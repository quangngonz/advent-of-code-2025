from task_1 import format_input


def main():
    fresh_ranges, items = format_input('day_5/input.txt')

    fresh_ranges.sort(axis=0)
    fresh_ranges = fresh_ranges.tolist()

    i = 0
    while i < len(fresh_ranges) - 1:
        current_range = fresh_ranges[i]
        next_range = fresh_ranges[i + 1]

        if current_range[1] >= next_range[0]:
            new_range = [current_range[0], max(
                current_range[1], next_range[1])]
            fresh_ranges[i] = new_range
            fresh_ranges.pop(i + 1)
        else:
            i += 1

    total = 0

    for top, bottom in fresh_ranges:
        total += bottom - top + 1

    print(f'Total fresh items: {total}')


if __name__ == '__main__':
    main()
