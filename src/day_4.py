def get_sections(str_section: str) -> set:
    section_start, section_end = [int(section) for section in str_section.split("-")]
    return set(range(section_start, section_end + 1))


def is_fully_overlapped_sections(section1: set, section2: set) -> bool:
    return section1.issubset(section2) | section2.issubset(section1)


def count_fully_overlapped_sections(section_assignments_list: list) -> int:
    overlap_count = 0
    for sections in section_assignments_list:
        section1, section2 = [get_sections(section_range) for section_range in sections.split(",")]
        if is_fully_overlapped_sections(section1, section2):
            overlap_count += 1
    return overlap_count


def main():
    with open("../input/day_4.txt") as input_file:
        section_assignments_list = input_file.read().splitlines()

        count_full_subset_section = count_fully_overlapped_sections(section_assignments_list)
        print(f"Full section overlaps: {count_full_subset_section}")


if __name__ == "__main__":
    main()
