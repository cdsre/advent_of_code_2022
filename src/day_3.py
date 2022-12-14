from string import ascii_lowercase, ascii_uppercase

priority_map = {v: i for i, v in enumerate(ascii_lowercase + ascii_uppercase, 1)}


def process_bag(bag: str) -> int:
    first_compartment = set(bag[:len(bag) // 2])
    second_compartment = set(bag[len(bag) // 2:])
    return [priority_map[v] for v in first_compartment & second_compartment][0]


def bags_priority(bags: list) -> int:
    total = 0
    for bag in bags:
        total += process_bag(bag)
    return total


def bags_group_priority(bags: list, group_size=3) -> int:
    total = 0
    for i in range(0, len(bags), group_size):
        group_bags = [set(bag) for bag in bags[i:i + group_size]]
        common = set.intersection(*group_bags)
        total += [priority_map[v] for v in common][0]
    return total


def main():
    with open("../input/day_3.txt") as input_file:
        bag_list = input_file.read().splitlines()
        print(f"bags_total: {bags_priority(bag_list)}")
        print(f"group_bags_total: {bags_group_priority(bag_list)}")

if __name__ == "__main__":
    main()