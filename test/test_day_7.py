from pytest import fixture
from src.day_7 import get_dir_sizes, get_dirs_totalling_below_n, get_space_to_delete


@fixture()
def sample_input_data() -> list[str]:
    return """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k""".splitlines()


@fixture()
def dir_sizes():
    return {'/': 48381165, '//a': 94853, '//a/e': 584, '//d': 24933642}


def test_build_filesystem_map(sample_input_data, dir_sizes):
    assert get_dir_sizes(sample_input_data) == dir_sizes


def test_get_dirs_totaling_below_n(dir_sizes):
    assert get_dirs_totalling_below_n(dir_sizes, 100000) == 95437


def test_get_space_to_delete(dir_sizes):
    assert get_space_to_delete(dir_sizes, 70_000_000, 30_000_000) == 24_933_642