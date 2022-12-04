from pytest import fixture, mark
from src.day_2 import get_points_from_round, confirmed_elf_strategy, try_elf_strategy, decode_round


@fixture()
def strategy_guide_list():
    return """A Y
B X
C Z""".splitlines()


@mark.parametrize("elf,me,score", [
    ("rock", "rock", 4),
    ("rock", "paper", 8),
    ("paper", "rock", 1)
])
def test_get_points_from_round(elf, me, score):
    assert get_points_from_round(elf, me) == score


@mark.parametrize("raw,decoded", [
    (["A", "X"], ("rock", "rock")),
    (["B", "Y"], ("paper", "paper")),
    (["C", "Z"], ("scissors", "scissors"))
])
def test_decode_round(raw, decoded):
    assert decode_round(raw) == decoded


def test_try_elf_strategy(strategy_guide_list):
    assert try_elf_strategy(strategy_guide_list) == 15


def test_confirmed_elf_strategy(strategy_guide_list):
    assert confirmed_elf_strategy(strategy_guide_list) == 12
