
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

    start_indices = [0] + np.cumsum([l + 1 for l in lengths]).tolist()
    res = 0

    for i, (op, length) in enumerate(zip(operations, lengths)):
        start = start_indices[i]

        operands_str = []
        for col in range(length):
            column_chars = "".join(line[start + col] for line in numbers)
            operands_str.append(column_chars)

        operands = np.array(operands_str, dtype=np.int64)

        if op == "+":
            res += np.sum(operands)
        elif op == "*":
            res += np.prod(operands)

    print(res)


if __name__ == "__main__":
    main()
