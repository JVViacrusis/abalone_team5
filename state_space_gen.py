"""This module contains functions to generate state space.

This module is taking a more procedural approach since we
won't be keeping any state. Just inputs and outputs for the most part. At most
there might be a simple data class or two.

to save compute resources, things we would have formally put as objects,
will instead be kept primitive. For example, the board state will have a
standard representation, however it will not be formalized as an object.
To aid in understanding and development in this file, definitions will
be put in this docstring

informal definitions:
    board dictionary format:
    {<column_letter as digit><row_digit> : <0(black) | 1(white)>}

    example:
    ["C5b, C6b, C7w"]
    ->
    {35:0, 36:0, 37:1}

    working with strings is a lot slower than working with ints
    so the string notation will be converted into ints like so:

    column_letter: a..i -> 1..9
    row_digit: remains 1..9
    color: 0 for black, 1 for white

"""
from pprint import pprint
import utils
import itertools

directions = {
    "NE" : 11,
    "E" : 1,
    "SE" : -10,
    "SW" : -11,
    "W" : -1,
    "NW" : 10
}


def generate_moves_and_resulting_boardstates(in_path: str,
                                             moves_path: str,
                                             boardstates_path: str) -> None:
    """Generates files for moves and board states given an input file."""
    board, player_turn = in_to_dict(in_path)
    # print("board: ")
    # pprint(board)
    utils.print_board(board)
    print(f"player_turn: {player_turn}")
    # print("board:", board)

    valid_marble_groups = gen_valid_marble_groups(board, player_turn)
    print("valid_marble_groups:", valid_marble_groups)
    # for group in valid_marble_groups:
    #     board_repped_group = {}
    #     for marble_coord in group:
    #         board_repped_group[marble_coord] = player_turn
    #     utils.print_board(board_repped_group)
    #     print("==============================")

    # moves = []
    # for group in valid_marble_groups:
    #     moves += gen_valid_group_moves(board, group)
    # print("valid_moves:", moves)


def in_to_dict(in_path: str) -> tuple[dict[int, int], int]:
    """Converts the input file into a dictionary of marbles and player turn.

    The input format is described in the project outline documentation
    and this function converts it into our desired board representation
    as described in this module's docstring under "board dictionary format"
    """
    with open(in_path, 'r') as f:
        player_turn = 0 if 'b' in f.readline() else 1

        board = {}
        for coord in f.readline().split(','):
            column_digit = (ord(coord[0]) - 64)
            row_digit = int(coord[1])
            color = 0 if coord[2] == 'b' else 1
            board[column_digit*10 + row_digit] = color

    return board, player_turn


def gen_valid_marble_groups(board: dict[int, int], color: int):
    """Generates valid marble groups for a given board state."""
    player_marbles = board.copy()
    _filter_for_color(player_marbles, color)
    print("player marbles:", player_marbles)
    coords = list(player_marbles.keys())
    print("coords:", coords)
    all_groups = _gen_combinations(coords)
    print("all_groups:", all_groups)

    _filter_for_valid_groups(all_groups)
    valid_groups = all_groups
    # print("valid_groups:", valid_groups)
    return valid_groups


def _filter_for_valid_groups(groups: list[tuple[int, ...]]):
    """Filters out invalid groups."""
    to_remove = []
    for i, group in enumerate(groups):
        if len(group) == 1:
            continue

        if len(group) == 2:
            valid_two_length = False
            # if not adjacent, invalid
            for dir_val in directions.values():
                if group[1] == group[0] + dir_val:
                    valid_two_length = True
                    break
            if not valid_two_length:
                to_remove.append(i)
            continue

        if len(group) == 3:
            valid_three_length = False

            for dir_val in directions.values():
                if (group[1] == group[0] + dir_val
                        and group[2] == group[0] + dir_val + dir_val):
                    valid_three_length = True

            # TODO: works for (34, 44, 54)(0, +10, +20)
            #  should also check for (34, 54, 44), (54, 34, 44) ...

            if not valid_three_length:
                to_remove.append(i)
            continue

    for i, combo_to_remove in enumerate(to_remove):
        groups.pop(combo_to_remove - i)


def _filter_for_color(board: dict[int, int], color: int):
    """In place, filters the board out for the colors we are looking for."""
    to_remove = []
    for key, value in board.items():
        if value != color:
            to_remove.append(key)

    for key in to_remove:
        del board[key]


def _gen_combinations(marble_coords: list[int]) -> list[tuple[int, ...]]:
    """Generates all combinations of length 1, 2, 3 given a set of coords.

    :return: The list of all combinations of length 1, 2, and 3
    :rtype: list[tuple[]]
    """
    len_1 = list(itertools.combinations(marble_coords, 1))
    len_2 = list(itertools.combinations(marble_coords, 2))
    len_3 = list(itertools.combinations(marble_coords, 3))
    return len_1 + len_2 + len_3


def gen_valid_group_moves(board: dict[int, int],
                          player_color: int,
                          group: tuple[int, ...]) -> tuple[list[int], int]:
    """Generates all valid moves."""
    broadside_dirs, inline_dirs = get_directions(group)
    # get broadside directions
    # get inline directions
    # gen_valid_broadsides(group, broadside_dirs)
    # gen_valid_inlines(group, inline_dirs)
    # return broadsides + inlines
    pass

def get_directions(group: tuple[int, ...]) -> tuple[list[int], list[int]]:
    """Determines the directions for broadside and inline moves."""
    pass


def gen_valid_broadsides(board: dict[int, int],
                         player_color: int,
                         group: tuple[int, ...],
                         dir_values: list[int]) -> tuple[list[int], int]:
    """Generates valid broadside moves."""
    pass


def gen_valid_inlines():
    """Generates valid inline moves."""
    pass


def _gen_broadsides():
    """Generates all broadside moves, valid or invalid."""
    pass


def gen_inlines():
    """Generates all inline moves, valid or invalid."""
    pass

if __name__ == "__main__":
    in_base = "data/in/"
    out_base = "data/out/"
    generate_moves_and_resulting_boardstates(in_base+"Test3.input",
                                             out_base+"test1.out.moves",
                                             out_base+"test1.out.board")

    # generate_moves_and_resulting_boardstates(in_base+"Test1.input",
    #                                          out_base+"test1.out.moves",
    #                                          out_base+"test1.out.board")
