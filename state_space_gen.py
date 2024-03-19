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


def generate_moves_and_resulting_boardstates(in_path: str,
                                             moves_path: str,
                                             boardstates_path: str) -> None:
    """Generates files for moves and board states given an input file."""
    board, player_turn = in_to_dict(in_path)
    print("board: ")
    pprint(board)
    print(f"player_turn: {player_turn}")
    utils.print_board(board)


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


def gen_valid_marble_groups(board: dict[str, int], color: int):
    """Generates valid marble groups for a given board state."""
    pass


def filter_for_color(board: dict[int, int], color: int):
    """In place, filters the board out for the colors we are looking for."""
    pass


def gen_valid_broadsides():
    """Generates valid broadside moves."""
    pass


def gen_valid_inlines():
    """Generates valid inline moves."""
    pass


def gen_broadsides():
    """Generates all broadside moves, valid or invalid."""
    pass


def gen_inlines():
    """Generates all inline moves, valid or invalid."""
    pass

if __name__ == "__main__":
    in_base = "data/in/"
    out_base = "data/out/"
    generate_moves_and_resulting_boardstates(in_base+"Test2.input",
                                             out_base+"test1.out.moves",
                                             out_base+"test1.out.board")

    generate_moves_and_resulting_boardstates(in_base+"Test1.input",
                                             out_base+"test1.out.moves",
                                             out_base+"test1.out.board")