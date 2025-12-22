import numpy as np


def format_input(filename):
    with open(filename, 'r') as file:
        lines = file.read().splitlines()

    # print(lines)

    return lines


def main():
    input_data = format_input('day_4/input.txt')
    input_data_np = np.array([list(line) for line in input_data])

    valid_count = 0
    valid_pos = []

    for idx_l, line in enumerate(input_data):
        for idx_c, char in enumerate(line):

            grid = input_data_np[
                max(0, idx_l - 1): idx_l + 2,
                max(0, idx_c - 1): idx_c + 2
            ]

            if char == '@' and (grid == '@').sum() < 5:
                valid_count += 1
                valid_pos.append((idx_l, idx_c))

    print(f"Valid positions: {valid_pos}")
    print(f"Valid count: {valid_count}")


if __name__ == "__main__":
    main()
