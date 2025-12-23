import numpy as np


def format_input(filename):
    with open(filename, 'r') as f:
        input_data = f.read().split('\n')

        operations = input_data.pop().split()
        numbers = [line.split() for line in input_data]

        return np.array(numbers, dtype='int64'), np.array(operations)


def main():
    numbers, operations = format_input('day_6/input.txt')

    addition_mask = operations == "+"
    add_no = np.sum(np.sum(numbers[:, addition_mask]))

    multiplication_mask = operations == "*"
    mult_no = np.sum(np.prod(numbers[:, multiplication_mask], axis=0))

    print(add_no + mult_no)


if __name__ == "__main__":
    main()
