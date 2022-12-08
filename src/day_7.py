def get_dir_sizes(command_output: list[str]) -> dict[str: int]:
    dir_sizes = {}
    dir_path = []
    for output in command_output:
        if output.startswith("$ ls") or output.startswith("dir"):
            continue
        if output.startswith("$ cd"):
            dir_name = output.split()[2]
            dir_path_str = "/".join([*dir_path, dir_name])
            if dir_name == "..":
                pop_dir_name = dir_path.pop()
                pop_dir_path_str = "/".join([*dir_path, pop_dir_name])
                dir_sizes["/".join(dir_path)] += dir_sizes[pop_dir_path_str]
            else:
                dir_path.append(dir_name)
                dir_sizes[dir_path_str] = 0
        else:
            size, filename = output.split()
            dir_sizes["/".join(dir_path)] += int(size)
    while len(dir_path) > 1:
        pop_dir_name = dir_path.pop()
        pop_dir_path_str = "/".join([*dir_path, pop_dir_name])
        dir_sizes["/".join(dir_path)] += dir_sizes[pop_dir_path_str]
    return dir_sizes


def get_dirs_totalling_below_n(dir_sizes: dict[str: int], n: int) -> int:
    return sum([size for size in dir_sizes.values() if size <= n])


def get_space_to_delete(dir_sizes: dict[str: int], total_space: int, needed_space: int):
    possible_delete_space = []
    free_space = total_space - dir_sizes["/"]
    for size in dir_sizes.values():
        if free_space + size > needed_space:
            possible_delete_space.append(size)

    return sorted(possible_delete_space)[0]


def main():
    with open("../input/day_7.txt") as input_file:
        input_data = input_file.read().splitlines()
        dir_sizes = get_dir_sizes(input_data)
        total_dirs_size = get_dirs_totalling_below_n(dir_sizes, 100000)
        print(f"{total_dirs_size=}")

        free_space = get_space_to_delete(dir_sizes, 70_000_000, 30_000_000)
        print(f"{free_space=}")


if __name__ == "__main__":
    main()
