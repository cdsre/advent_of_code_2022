from pytest import fixture
from src.day_3 import bags_priority, process_bag, bags_group_priority


@fixture()
def bags_contents():
    return """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw""".splitlines()


def test_process_bag():
    assert process_bag("abcxbz") == 2


def test_bags_priority(bags_contents):
    assert bags_priority(bags_contents) == 157


def test_bags_group_priority(bags_contents):
    assert bags_group_priority(bags_contents) == 70
