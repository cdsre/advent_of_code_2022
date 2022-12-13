from pytest import fixture, mark
from src.day_11 import parse_monkeys_data, parse_monkey_data, parse_starting_items, parse_operation, parse_test, \
    parse_if, monkey_business


def test_parse_monkeys_data(monkeys_data, split_monkeys_data):
    assert parse_monkeys_data(monkeys_data) == split_monkeys_data


# def test_monkey_business(split_monkeys_data):
#     monkeys = [parse_monkey_data(monkey_data) for monkey_data in split_monkeys_data]
#     assert monkey_business(monkeys) == 10605
#

def test_monkey_business2(split_monkeys_data):
    monkeys = [parse_monkey_data(monkey_data) for monkey_data in split_monkeys_data]
    assert monkey_business(monkeys, 10000, 1, 96577) == 2713310158


@mark.parametrize("data,result", (
        ("Starting items: 79, 98", {"Starting items": [79, 98]}),
        ("Starting items: 54, 65, 75, 74", {"Starting items": [54, 65, 75, 74]}),
        ("Starting items: 74", {"Starting items": [74]}),
        ("Starting items: ", {"Starting items": []}),
))
def test_parse_starting_items(data, result):
    assert parse_starting_items(data) == result


@mark.parametrize("operation, old, result", (
        ("Operation: new = old * 19", 10, 190),
        ("Operation: new = old + 6", 10, 16),
        ("Operation: new = old * old", 10, 100),
        ("Operation: new = old - 3", 10, 7),
        ("Operation: new = old / 2", 10, 5),

))
def test_parse_operation(operation, old, result):
    assert parse_operation(operation)["Operation"](old) == result


@mark.parametrize("operation, new, result", (
        ("Test: divisible by 10", 100, True),
        ("Test: divisible by 23", 100, False),
        ("Test: divisible by 55", 100, False),
))
def test_parse_test(operation, new, result):
    assert parse_test(operation)["Test"](new) == result


@mark.parametrize("if_data, result", (
        ("If true: throw to monkey 0", {True: "0"}),
        ("If false: throw to monkey 0", {False: "0"}),
        ("If true: throw to monkey 100", {True: "100"}),
))
def test_parse_if(if_data, result):
    assert parse_if(if_data) == result


@fixture()
def monkeys_data():
    return """Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1"""


@fixture()
def split_monkeys_data():
    return [
        """Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3
""",

        """Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0
""",

        """Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3
""",

        """Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1
"""
    ]
