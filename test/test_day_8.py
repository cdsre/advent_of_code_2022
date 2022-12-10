from pytest import fixture, mark
from src.day_8 import how_many_visable_trees, is_visible, generate_gyro_map, get_west_trees, get_east_trees, \
    get_north_trees, get_south_trees, get_scenic_score, get_tree_scenic_score


@fixture()
def tree_data() -> str:
    return """30373
25512
65332
33549
35390"""


@fixture()
def gyro_map() -> list[list[int]]:
    return [
        [3, 0, 3, 7, 3],
        [2, 5, 5, 1, 2],
        [6, 5, 3, 3, 2],
        [3, 3, 5, 4, 9],
        [3, 5, 3, 9, 0]
    ]


TREE_PARAM_DATA = "x, y, trees", (
    (0, 0, [0, 3, 7, 3]),
    (2, 3, [4, 9]),
    (4, 1, []),
    (4, 4, [])
)


@mark.parametrize("trees, tree_size, result", (
        ([2, 3, 4, 5], 1, False),
        ([2, 3, 4, 5], 5, False),
        ([2, 3, 4, 5], 6, True),
        ([], 3, True)
))
def test_is_visible(trees, tree_size, result):
    assert is_visible(trees, tree_size) == result


@mark.parametrize("x, y, trees", (
        (0, 0, []),
        (2, 3, [3, 3]),
        (4, 1, [2, 5, 5, 1]),
        (4, 4, [3, 5, 3, 9])
))
def test_get_west_tress(gyro_map, x, y, trees):
    assert get_west_trees(gyro_map, x, y) == trees


@mark.parametrize("x, y, trees", (
        (0, 0, [0, 3, 7, 3]),
        (2, 3, [4, 9]),
        (4, 1, []),
        (4, 4, [])
))
def test_get_east_tress(gyro_map, x, y, trees):
    assert get_east_trees(gyro_map, x, y) == trees


@mark.parametrize("x, y, trees", (
        (0, 0, []),
        (2, 3, [3, 5, 3]),
        (4, 1, [3]),
        (4, 4, [3, 2, 2, 9])
))
def test_get_north_tress(gyro_map, x, y, trees):
    assert get_north_trees(gyro_map, x, y) == trees


@mark.parametrize("x, y, trees", (
        (0, 0, [2, 6, 3, 3]),
        (2, 3, [3]),
        (4, 1, [2, 9, 0]),
        (4, 4, [])
))
def test_get_south_tress(gyro_map, x, y, trees):
    assert get_south_trees(gyro_map, x, y) == trees


def test_generate_gyro_map(tree_data, gyro_map):
    assert generate_gyro_map(tree_data) == gyro_map


def test_how_many_visable_trees(gyro_map):
    assert how_many_visable_trees(gyro_map) == 21


def test_get_scenic_score(gyro_map):
    assert get_scenic_score(gyro_map) == 8


@mark.parametrize("x, y, score", (
        (2, 1, 4),
))
def test_get_tree_scenic_score(gyro_map, x, y, score):
    assert get_tree_scenic_score(gyro_map, x, y) == score
