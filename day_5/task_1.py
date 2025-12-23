import numpy as np


def format_input(filename):
    with open(filename, "r") as file:
        valid_ranges, items = file.read().split('split_char')

        valid_ranges = valid_ranges.split('\n')
        items = items.split('\n')

    valid_ranges = [ranges.split("-") for ranges in valid_ranges]
    valid_ranges.pop()
    items.pop(0)

    return np.array(valid_ranges, dtype='int64'), np.array(items, dtype='int64')


def main():
    valid_ranges, items = format_input('day_5/input.txt')

    fresh_item = []

    for item in items:
        for bottom, top in valid_ranges:
            if bottom < item < top:
                fresh_item.append(item)
                break

    print(f'Number Fresh Items: {len(fresh_item)}')


if __name__ == "__main__":
    main()
