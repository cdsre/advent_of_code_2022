def detect_start_marker(signal: str, sequence_length=4) -> int:
    for i in range(len(signal)):
        seq = signal[i:i + sequence_length]
        set_seq = set(seq)
        if len(set_seq) == sequence_length:
            return i + sequence_length
    return -1


def main():
    with open("../input/day_6.txt") as input_file:
        signal = input_file.readline()

        start_marker = detect_start_marker(signal)
        print(f"{start_marker=}")

        message_marker = detect_start_marker(signal, sequence_length=14)
        print(f"{message_marker=}")


if __name__ == "__main__":
    main()
