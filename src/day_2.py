options = ["rock", "paper", "scissors"]
elf_hand = dict(zip(["A", "B", "C"], options))
my_hand = dict(zip(["X", "Y", "Z"], options))
winning_hands = {
    "rock": "scissors",
    "scissors": "paper",
    "paper": "rock"
}
losing_hands = {v: k for k, v in winning_hands.items()}

score_map = {
    "rock": 1,
    "paper": 2,
    "scissors": 3
}


def decode_round(player_hands: list) -> tuple:
    elf, me = player_hands
    return elf_hand[elf], my_hand[me]


def get_points_from_round(elf: str, me: str) -> int:
    points = score_map[me]
    if winning_hands[me] == elf:
        points += 6
    if elf == me:
        points += 3
    return points


def try_elf_strategy(rounds: list) -> int:
    total_points = 0
    for current_round in rounds:
        elf, me = decode_round(current_round.split())
        total_points += get_points_from_round(elf, me)
    return total_points


def confirmed_elf_strategy(rounds: list) -> int:
    total_points = 0
    for current_round in rounds:
        raw_elf, raw_me = current_round.split()
        elf, me = decode_round([raw_elf, raw_me])

        # change our hand based on the new code
        if raw_me == "X":
            me = winning_hands[elf]
        elif raw_me == "Y":
            me = elf
        else:
            me = losing_hands[elf]
        total_points += get_points_from_round(elf, me)
    return total_points


def main():
    with open("../input/day_2.txt") as input_file:
        rounds = input_file.read().splitlines()

        try_strategy_points = try_elf_strategy(rounds)
        print(f"try_strategy_score: {try_strategy_points}")

        confirm_strategy_points = confirmed_elf_strategy(rounds)
        print(f"confirmed_strategy_score: {confirm_strategy_points}")


if __name__ == "__main__":
    main()
