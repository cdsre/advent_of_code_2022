from src.day_6 import detect_start_marker
from pytest import mark


@mark.parametrize("signal,start_marker, message_marker", (
        ("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 7, 19),
        ("bvwbjplbgvbhsrlpgdmjqwftvncz", 5, 23),
        ("nppdvjthqldpwncqszvftbrmjlhg", 6, 23),
        ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 10, 29),
        ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 11, 26),
))
def test_detect_start_marker(signal, start_marker, message_marker):
    assert detect_start_marker(signal, 4) == start_marker
    assert detect_start_marker(signal, 14) == message_marker
