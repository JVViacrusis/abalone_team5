"""This module contains functions to generate state space.

This module is taking a more procedural approach since we
won't be keeping any state. Just inputs and outputs for the most part. At most
there might be a simple data class or two.

to save compute resources, things we would have formally put as objects,
will instead be kept primitive. For example, the board state will have a
standard representation, however it will not be formalized as an object.
To aid in understanding and development in this file, definitions will
be put in this docstring

Informal Definition, and Conventions:

    BOARD DICTIONARY FORMAT:
        a dictionary representation of the board, with each marble
        being a coordinate plus colour formatted like so:
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


    DELTAS AND DIRECTIONS:
        a delta is the positional change associated with a direction:
            <row_change_digit><column_change_digit>:<direction_string>

        example:
            11:"NE" means "row add 1, column add 1 : is North-East"

                 10:NW     11:NE
                     \     /
                      ⟋  ⟍
            -01:W --  ⎸  ⎹  -- 01:E
                      ⟍  ⟋
                     /     \
                -11:SW    -10:SE


    GROUP:
        a combination of 1, 2, or 3 marbles formatted like so:
            ((<marble_coord>:<marble_color>, ...), delta)

        examples:
            (34, 33, 37)
            (23,)
            (21, 32)


    GROUPMOVE:
        a groupmove is a group of marbles moving in a certain direction
        with the following format:
            ((marble1, ...), delta)

        example:


    GENALL VS DERIVE:
        genall, short for 'generate all', generates all of something,
        derive generates one or a subset of something

        example:
            genall_groupmove generates all groupmoves
            derive_groupmove generates one or a small subset of groupmoves
"""
from pprint import pprint
import debugutils
import external


def genall_groupmove_resultboard(marbles: dict[int, int],
                                 player_color: int)\
        -> list[tuple[tuple[tuple[dict[int, int], ...], int], dict[int, int]]]:
    """Generates all groupmoves and the resulting board from those moves.

    return format explained:
        output = list[(groupmove, resultant_board)]

        groupmove = (group, direction)
        resultant_board = list[marble]

        group = (marble, ...)
        direction = int

        marble = {coord : color, ...}

        coord = int
        color = int
    """
    debugutils.print_board(marbles)
    # print("marbles:")
    # pprint(marbles)
    # print("player_color:", player_color)

    player_marbles = filter_for_color(marbles, player_color)
    pprint(player_marbles)


def filter_for_color(marbles: dict[int, int], color: int):
    """filters the board out for the colors we are looking for."""
    return dict(filter(lambda marble: marble[1] == color, marbles.items()))


if __name__ == "__main__":
    in_base = "data/in/"
    out_base = "data/out/"

    board_marbles, player_color = external.in_to_marbles(in_base+"Test1.input")
    result = genall_groupmove_resultboard(board_marbles, player_color)
    print("groupmoves_resultboards:", result)

    # board_marbles, player_color = external.in_to_marbles(in_base+"Test2.input")
    # result = genall_groupmove_resultboard(board_marbles, player_color)
    # print("groupmoves_resultboards:", result)