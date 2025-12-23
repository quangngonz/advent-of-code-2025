import numpy as np


def format_input(filename):
    with open(filename, 'r') as f:
        input_data = f.read().split('\n')

        operations = input_data.pop().split()
        numbers = [line.split() for line in input_data]

        return np.array(numbers, dtype='int64'), operations


def main():
    numbers, operations = format_input('day_6/input.txt')

    sum_matrix = np.sum(numbers, axis=0)
    multiplication_matrix = np.prod(numbers, axis=0)

    total = 0

    for idx, op in enumerate(operations):
        if op == "+":
            total += sum_matrix[idx]
        elif op == "*":
            total += multiplication_matrix[idx]
        else:
            print("Error", op)

    print(total)


if __name__ == "__main__":
    main()
