import re


def get_initial_stacks(crane_procedure: list) -> dict[list]:
    # capture the stacks only
    stacks = []
    for line in crane_procedure:
        if line == "":
            break
        stacks.append(line)

    # transpose the stacks and pick only those that start with a number
    trans_stack = list(zip(*stacks[::-1]))
    stacks = {s[0]: list(s[1:]) for s in zip(*stacks[::-1]) if s[0].isdigit()}

    # pop any empty items in the stack
    for stack in stacks.values():
        while stack[-1] == " ":
            stack.pop()

    return stacks


def parse_move_instruction(move_instruction: str) -> list:
    match = re.findall(r"(\d+)", move_instruction)
    return match


def get_move_instructions(crane_procedure: list) -> list:
    split_point = crane_procedure.index("")
    return crane_procedure[split_point + 1:]


def process_move_instruction(stacks: dict[str, list], num_crates, from_stack, to_stack) -> None:
    for _ in range(int(num_crates)):
        stacks[to_stack].append(stacks[from_stack].pop())


def execute_crane_procedure(stacks, move_instructions):
    for move in move_instructions:
        num_crates, from_stack, to_stack = parse_move_instruction(move)
        process_move_instruction(stacks, num_crates, from_stack, to_stack)


def get_top_of_stacks(stacks):
    return [stack[-1] for stack in stacks.values()]


def rearrange_and_get_top_stacks(crane_procedure):
    stacks = get_initial_stacks(crane_procedure)
    moves = get_move_instructions(crane_procedure)
    execute_crane_procedure(stacks, moves)
    return "".join(get_top_of_stacks(stacks))


def main():
    with open("../input/day_5.txt") as input_file:
        crane_procedure = input_file.read().splitlines()
        top_after_rearrange = rearrange_and_get_top_stacks(crane_procedure)
        print(f"{top_after_rearrange=}")


if __name__ == "__main__":
    main()
