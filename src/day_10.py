def signal_strength(signal_data: list[str], key_cycles=(20, 60, 100, 140, 180, 220)):
    cycle = 1
    x = 1
    signal_value = 0
    for signal in signal_data:
        if cycle in key_cycles:
            print(f"{cycle=},{x=}")
            signal_value += (cycle * x)
        if signal.startswith("addx"):
            cycle += 1
            if cycle in key_cycles:
                print(f"{cycle=},{x=}")
                signal_value += cycle * x
            x += int(signal.split()[1])
        cycle += 1

    return signal_value


def draw_screen(signal_data):
    cycle = 1
    x = 1
    screen = ""
    for signal in signal_data:
        screen += draw_pixel(cycle, x)
        if signal.startswith("addx"):
            cycle += 1
            screen += draw_pixel(cycle, x)
            x += int(signal.split()[1])
        cycle += 1

    print(screen)
    return screen.strip()


def draw_pixel(cycle, register):
    position = cycle % 40
    sprite = list(range(register, register + 3))
    if sprite[-1] == 40:
        sprite[-1] = 0
    if position in sprite:
        pixel = "#"
    else:
        pixel = "."

    print(f"{cycle=},{register=},{position=},{pixel=}")
    return f"{pixel}\n" if position == 0 else pixel


def main():
    with open("../input/day_10.txt") as input_file:
        signal_data = input_file.read().splitlines()
        signal = signal_strength(signal_data)
        print(f"{signal=}")

        screen = draw_screen(signal_data)
        print(f"{screen=}")


if __name__ == "__main__":
    main()
