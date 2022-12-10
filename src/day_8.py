def is_visible(trees: list[int], tree_size: int) -> bool:
    if trees and max(trees) >= tree_size:
        return False
    return True


def generate_gyro_map(tree_data: str) -> list[list[int]]:
    return [[int(height) for height in row] for row in tree_data.splitlines()]


def get_west_trees(gyro_map: list[list[int]], x: int, y: int) -> list[int]:
    return gyro_map[y][:x]


def get_east_trees(gyro_map: list[list[int]], x: int, y: int) -> list[int]:
    return gyro_map[y][x + 1:]


def get_north_trees(gyro_map: list[list[int]], x: int, y: int) -> list[int]:
    trans_map = list(zip(*gyro_map))
    return list(trans_map[x][:y])


def get_south_trees(gyro_map: list[list[int]], x: int, y: int) -> list[int]:
    trans_map = list(zip(*gyro_map))
    return list(trans_map[x][y + 1:])


def how_many_visable_trees(gyro_map) -> int:
    visible_trees = 0
    for y in range(len(gyro_map)):
        for x in range(len(gyro_map[0])):
            trees = [
                get_west_trees(gyro_map, x, y),
                get_east_trees(gyro_map, x, y),
                get_north_trees(gyro_map, x, y),
                get_south_trees(gyro_map, x, y)
            ]

            for tree_line in trees:
                if not tree_line or max(tree_line) < gyro_map[y][x]:
                    visible_trees += 1
                    break
    return visible_trees


def get_tree_scenic_score(gyro_map: list[list[int]], x, y) -> int:
    tree = gyro_map[y][x]
    tree_score = 1
    trees = [
        get_west_trees(gyro_map, x, y)[::-1],
        get_east_trees(gyro_map, x, y),
        get_north_trees(gyro_map, x, y)[::-1],
        get_south_trees(gyro_map, x, y)
    ]

    for tree_line in trees:
        for i, v in enumerate(tree_line, 1):
            if v >= tree:
                tree_score *= i
                break
        else:
            tree_score *= len(tree_line) if tree_line else 0
    return tree_score


def get_scenic_score(gyro_map: list[list[int]]) -> int:
    scenic_score = 0
    for y in range(len(gyro_map)):
        for x in range(len(gyro_map[0])):
            tree_score = get_tree_scenic_score(gyro_map, x, y)

            if tree_score > scenic_score:
                scenic_score = tree_score

            # print(f"{y=},{x=},{tree_score=}")
    return scenic_score


def main():
    with open("../input/day_8.txt") as input_file:
        gyro_map = generate_gyro_map(input_file.read())
        visible_trees = how_many_visable_trees(gyro_map)
        print(f"{visible_trees=}")
        scenic_score = get_scenic_score(gyro_map)
        print(f"{scenic_score=}")


if __name__ == "__main__":
    main()
