def move_head(x: int, y: int, direction: str, spaces: int) -> tuple[int, int]:
    if direction == "R":
        return x + spaces, y
    if direction == "L":
        return x - spaces, y
    if direction == "U":
        return x, y + spaces
    if direction == "D":
        return x, y - spaces


def move_tail(head_x: int, head_y: int, tail_x: int, tail_y: int) -> tuple[int, int]:
    if head_x == tail_x and abs(head_y - tail_y) > 1:
        if head_y - tail_y > 0:
            return tail_x, head_y - 1
        return tail_x, head_y + 1

    if head_y == tail_y and abs(head_x - tail_x) > 1:
        if head_x - tail_x > 0:
            return head_x - 1, tail_y
        return head_x + 1, tail_y

    x_diff = head_x - tail_x
    y_diff = head_y - tail_y

    if abs(x_diff) > 1 and abs(y_diff) > 1:
        if x_diff > 0:
            x = head_x - 1
        else:
            x = head_x + 1

        if y_diff > 0:
            y = head_y - 1
        else:
            y = head_y + 1
        return x, y
    if abs(x_diff) > 1:
        if x_diff > 0:
            return head_x - 1, head_y
        return head_x + 1, head_y

    if abs(y_diff) > 1:
        if y_diff > 0:
            return head_x, head_y - 1
        return head_x, head_y + 1

    return tail_x, tail_y


def count_tail_squares(head_moves: list[str]) -> int:
    tail_squares = {(0, 0)}
    head_x, head_y = 0, 0
    tail_x, tail_y = 0, 0
    for move in head_moves:
        direction, spaces = move.split()
        for _ in range(int(spaces)):
            head_x, head_y = move_head(head_x, head_y, direction, 1)
            tail_x, tail_y = move_tail(head_x, head_y, tail_x, tail_y)
            tail_squares.add((tail_x, tail_y))
    return len(tail_squares)


def count_last_knot_squares(head_moves: list[str], knot_count=9) -> int:
    knots = [{"x": 0, "y": 0, "squares": {(0, 0)}} for _ in range(knot_count)]
    head_x, head_y = 0, 0

    for move in head_moves:
        direction, spaces = move.split()
        #print(f"{direction=},{spaces=}")
        for _ in range(int(spaces)):
            head_x, head_y = move_head(head_x, head_y, direction, 1)
            for index, knot in enumerate(knots):
                if index == 0:
                    knot["x"], knot["y"] = move_tail(head_x, head_y, knot["x"], knot["y"])
                else:
                    knot["x"], knot["y"] = move_tail(knots[index - 1]["x"], knots[index - 1]["y"], knot["x"], knot["y"])
                knot["squares"].add((knot["x"], knot["y"]))
        #print("####")
        #generate_grid(knots, head_y, head_x)
    return len(knots[-1]["squares"])


def generate_grid(knots, head_y, head_x):
    x_vals = [knot["x"] for knot in knots]
    y_vals = [knot["y"] for knot in knots]
    min_x = min(x_vals)
    max_x = max(x_vals)
    min_y = min(y_vals)
    max_y = max(y_vals)

    grid = [["." for _ in range(50)] for _ in range(50)]
    grid[head_y+25][head_x+25] = "H"
    for i, knot in enumerate(knots, 1):
        if grid[knot["y"]+25][knot["x"]+25] == ".":
            grid[knot["y"]+25][knot["x"]+25] = str(i)
    print("\n".join([" ".join(row) for row in grid[::-1]]))


def main():
    with open("../input/day_9.txt") as input_file:
        head_moves = input_file.read().splitlines()
        tail_squares = count_tail_squares(head_moves)
        print(f"{tail_squares=}")
        last_knot_squares = count_last_knot_squares(head_moves)
        print(f"{last_knot_squares=}")


if __name__ == "__main__":
    main()
