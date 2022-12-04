from pytest import fixture
from src.day_1 import get_most_calories, get_top_3_calories_sum, get_calories_per_elf


@fixture()
def calories_list():
    return """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000""".splitlines()


@fixture()
def calories_per_elf(calories_list):
    return get_calories_per_elf(calories_list)


def test_calories_per_elf(calories_list):
    calories_per_elf = get_calories_per_elf(calories_list)
    assert calories_per_elf == [6000, 4000, 11000, 24000, 10000]


def test_get_most_calories(calories_per_elf):
    assert get_most_calories(calories_per_elf) == 24000

def test_get_top_3_calories_sum(calories_per_elf):
    assert get_top_3_calories_sum(calories_per_elf) == 45000
