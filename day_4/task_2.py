from task_1 import format_input
import numpy as np


def main():
    input_data = format_input('day_4/input.txt')
    input_data_np = np.array([list(line) for line in input_data])

    removed_rolls = True
    roll_removed = 0

    while removed_rolls:
        removed_rolls = False
        valid_count = 0
        valid_pos = []

        for idx_l, line in enumerate(input_data_np):
            for idx_c, char in enumerate(line):
                # Check surrounding characters
                surrounding = input_data_np[
                    max(0, idx_l - 1): idx_l + 2,
                    max(0, idx_c - 1): idx_c + 2
                ]

                if char == '@' and np.count_nonzero(surrounding == '@') < 5:
                    valid_count += 1
                    valid_pos.append((idx_l, idx_c))
                    input_data_np[idx_l, idx_c] = '.'
                    removed_rolls = True
                    roll_removed += 1

        print(f"Valid positions this round: {valid_pos}")
        print(f"Valid count this round: {valid_count}")
    print(f"Total rolls removed: {roll_removed}")


if __name__ == "__main__":
    main()
