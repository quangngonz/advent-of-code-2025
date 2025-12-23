
import numpy as np


def format_input(filename):
    with open(filename, 'r') as f:
        input_data = f.read().split('\n')

        operations = input_data.pop()
        operations_formatted = operations.split()

        lengths = []
        len_c = 0
        for char in operations[1:]:
            if char in "+*":
                lengths.append(len_c)
                len_c = 0
            else:
                len_c += 1
        else:
            lengths.append(len_c+1)

        return np.array(input_data), np.array(operations_formatted), lengths


def main():
    numbers, operations, lengths = format_input('day_6/input.txt')

    lines_segmented = []

    for line in numbers:
        idx = 0
        lines_segmented.append([])
        for length in lengths:
            segment = line[idx:idx + length]
            lines_segmented[-1].append(segment)
            idx += length + 1
        else:
            segment = line[idx:]
            lines_segmented[-1].append(segment)

    lines_segmented = np.array(lines_segmented).T

    matrix_cleaned = []

    print(len(lines_segmented), len(operations), len(lengths))

    for numbers, operation, length in zip(lines_segmented, operations, lengths):

        operands = []

        for i in range(length):
            digits = [num[i] for num in numbers]
            operands.append(''.join(digits))

        operands = np.array(operands).astype(np.int64)

        matrix_cleaned.append((operation, operands))

    print(matrix_cleaned)

    res = 0

    for op, operands in matrix_cleaned:
        if op == "+":
            res += np.sum(operands)
        elif op == "*":
            res += np.prod(operands)

    print(res)


if __name__ == "__main__":
    main()
