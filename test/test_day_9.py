from pytest import fixture, mark
from src.day_9 import count_tail_squares, move_head, move_tail, count_last_knot_squares


@fixture()
def head_data():
    return """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2""".splitlines()


@mark.parametrize("x, y, direction, spaces, result", (
        (0, 0, "L", "2", (-2, 0)),
        (0, 0, "R", "2", (2, 0)),
        (0, 0, "U", "2", (0, 2)),
        (0, 0, "D", "2", (0, -2)),
))
def test_move_head(x, y, direction, spaces, result):
    assert move_head(x, y, direction, int(spaces)) == result


@mark.parametrize("head_x, head_y, tail_x, tail_y, result", (
        (-2, 0, 0, 0, (-1, 0)),
        (2, 0, 0, 0, (1, 0)),
        (0, 2, 0, 0, (0, 1)),
        (0, -2, 0, 0, (0, -1)),
        (2, 4, 4, 3, (3, 4))
))
def test_move_tail(head_x, head_y, tail_x, tail_y, result):
    assert move_tail(head_x, head_y, tail_x, tail_y) == result


def test_count_tail_squares(head_data):
    assert count_tail_squares(head_data) == 13


def test_last_knot_squares(head_data):
    assert count_last_knot_squares(head_data) == 1

def test_last_knot_squares_motion():
    assert count_last_knot_squares("""R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20""".splitlines()) == 1
