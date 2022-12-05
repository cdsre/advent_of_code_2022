import re

CRANE_MODEL = 9000


def get_initial_stacks(crane_procedure: list) -> dict[list]:
    # capture the stacks only
    split_point = crane_procedure.index("")
    stacks = crane_procedure[:split_point]

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


def process_move_instruction(stacks: dict[str, list], num_crates, from_stack, to_stack, model=CRANE_MODEL) -> None:
    move_stack = []
    for _ in range(int(num_crates)):
        move_stack.append(stacks[from_stack].pop())

    if model == 9001:
        move_stack = reversed(move_stack)

    stacks[to_stack] += move_stack


def execute_crane_procedure(stacks, move_instructions, model=CRANE_MODEL):
    for move in move_instructions:
        num_crates, from_stack, to_stack = parse_move_instruction(move)
        process_move_instruction(stacks, num_crates, from_stack, to_stack, model=model)


def get_top_of_stacks(stacks):
    return [stack[-1] for stack in stacks.values()]


def rearrange_and_get_top_stacks(crane_procedure, model=CRANE_MODEL):
    stacks = get_initial_stacks(crane_procedure)
    moves = get_move_instructions(crane_procedure)
    execute_crane_procedure(stacks, moves, model=model)
    return "".join(get_top_of_stacks(stacks))


def main():
    with open("../input/day_5.txt") as input_file:
        crane_procedure = input_file.read().splitlines()
        top_after_rearrange_9000 = rearrange_and_get_top_stacks(crane_procedure, model=9000)
        print(f"{top_after_rearrange_9000=}")

        top_after_rearrange_9001 = rearrange_and_get_top_stacks(crane_procedure, model=9001)
        print(f"{top_after_rearrange_9001=}")


if __name__ == "__main__":
    main()
