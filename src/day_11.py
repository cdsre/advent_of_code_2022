import operator
from ast import literal_eval

ACTIONS = {
    "*": operator.mul,
    "/": operator.truediv,
    "//": operator.floordiv,
    "+": operator.add,
    "-": operator.sub
}

NUM_ROUNDS = 20


def parse_starting_items(starting_items: str) -> dict:
    key, items = starting_items.split(':')
    return {key: [int(item) for item in items.split(",") if item.strip().isdigit()]}


def parse_operation(operation_data: str) -> dict:
    key, operation_str = operation_data.split(":")
    _, operation_action = operation_str.split("=")
    a, action, b = operation_action.strip().split()
    if a == b:
        return {key: lambda x: ACTIONS[action](x, x)}
    return {key: lambda x: ACTIONS[action](x, int(b))}


def parse_test(test_data: str) -> dict:
    key, test_str = test_data.split(":")
    denominator = int(test_str.split()[-1])
    return {key: lambda x: x % denominator == 0}


def parse_if(if_data):
    temp_key, throw_to = if_data.split(":")
    boolean = temp_key.split()[-1]
    monkey = throw_to.split()[-1]
    return {literal_eval(boolean.title()): monkey}


def parse_monkeys_data(monkeys_data: str) -> list[str]:
    monkey_data = [""]
    for line in monkeys_data.splitlines():
        if line:
            monkey_data[-1] += f"{line}\n"
        else:
            monkey_data.append("")
    return monkey_data


def parse_monkey_data(monkey_data: str):
    monkey_data_dict = {}
    for data in monkey_data.splitlines():
        data = data.strip()
        if data.startswith("Starting items"):
            monkey_data_dict.update(parse_starting_items(data))
        if data.startswith("Operation"):
            monkey_data_dict.update(parse_operation(data))
        if data.startswith("Test"):
            monkey_data_dict.update(parse_test(data))
        if data.startswith("If"):
            monkey_data_dict.update(parse_if(data))
    return monkey_data_dict


def monkey_business(monkeys, rounds=NUM_ROUNDS, worry_modifier=3, mod_reducer=1):
    monkey_items_counts = [0 for _ in range(len(monkeys))]
    for round in range(rounds):
        #print(round)
        for index, monkey in enumerate(monkeys):
            #print(round, index, monkey)
            for item in monkey["Starting items"]:
                monkey_items_counts[index] += 1
                new_item = (monkey["Operation"](item) // worry_modifier) % mod_reducer
                test_result = monkey["Test"](new_item)
                new_monkey = int(monkey[test_result])
                monkeys[new_monkey]["Starting items"].append(new_item)
            monkey["Starting items"] = []

        if round + 1 in [1, 20, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]:
            print(round + 1, monkey_items_counts)

    m1, m2 = sorted(monkey_items_counts)[-2:]
    return m1 * m2


def main():
    with open("../input/day_11.txt") as input_file:
        monkeys_data_str = input_file.read()
        monkeys_data = parse_monkeys_data(monkeys_data_str)
        monkeys = [parse_monkey_data(monkey) for monkey in monkeys_data]
        monkey_busi = monkey_business(monkeys)
        print(f"{monkey_busi=}")

        # calculated the LCM by hand to set the mod_reducer, this is needed because the numbers grow exponentionally
        # slowing down the computations
        monkeys = [parse_monkey_data(monkey) for monkey in monkeys_data]
        monkey_busi2 = monkey_business(monkeys, rounds=10_000, worry_modifier=1, mod_reducer=9699690)
        print(f"{monkey_busi2=}")


if __name__ == "__main__":
    main()
