from pytest import fixture, mark
from src.day_4 import get_sections, is_fully_overlapped_sections, count_fully_overlapped_sections, \
    count_any_overlapped_sections


@fixture()
def section_assignments_list():
    return """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8""".splitlines()


def test_get_sections():
    assert get_sections("3-8") == {3, 4, 5, 6, 7, 8}


@mark.parametrize("section1,section2,result", [
    ({1, 2, 3, 4, 5}, {2, 3, 4, 5}, True),
    ({1, 2, 3, 4, 5}, {4, 5, 6}, False),
    ({2, 3, 4}, {1, 2, 3, 4, 5}, True)
])
def test_is_fully_overlapped_sections(section1, section2, result):
    assert is_fully_overlapped_sections(section1, section2) is result


def test_count_fully_overlapped_sections(section_assignments_list):
    assert count_fully_overlapped_sections(section_assignments_list) == 2


def test_count_any_overlapped_sections(section_assignments_list):
    assert count_any_overlapped_sections(section_assignments_list) == 4
