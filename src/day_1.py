def get_calories_per_elf(calories: list[str]) -> list:
    calories_per_elf = [0]
    for calorie in calories:
        if calorie.isdigit():
            calories_per_elf[-1] += int(calorie)
        else:
            calories_per_elf.append(0)
    return calories_per_elf


def get_most_calories(calories_per_elf: list) -> int:
    return max(calories_per_elf)


def get_top_3_calories_sum(calories_per_elf: list) -> int:
    return sum(sorted(calories_per_elf)[-3:])


def main():
    with open("../input/day_1.txt") as input_file:
        calories_per_elf = get_calories_per_elf(input_file.read().splitlines())

        # get the most calories an elf is carrying
        most = max(calories_per_elf)
        print(f"Most calories: {most}")

        # get the sum of the top 3 elfs calories
        top_3_sum = sum(sorted(calories_per_elf)[-3:])
        print(f"top 3 total: {top_3_sum}")


if __name__ == "__main__":
    main()
