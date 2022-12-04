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


def test_elf_strategy(rounds: list) -> None:
    total_points = 0
    for current_round in rounds:
        elf, me = decode_round(current_round.split())
        total_points += get_points_from_round(elf, me)
    print(f"test_strategy_score: {total_points}")


def confirmed_elf_strategy(rounds: list) -> None:
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
    print(f"confirmed_strategy_score: {total_points}")


with open("../input/day_2.txt") as input_file:
    rounds = input_file.read().splitlines()
    test_elf_strategy(rounds)
    confirmed_elf_strategy(rounds)