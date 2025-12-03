from task_1 import format_input


def find_largest_cells(bank, digits_required=12):
    if digits_required == 0:
        return ""

    search_limit = len(bank) - digits_required + 1

    best_digit = -1
    best_index = -1

    for i in range(search_limit):
        val = int(bank[i])
        if val > best_digit:
            best_digit = val
            best_index = i

            if best_digit == 9:
                break

    return str(best_digit) + find_largest_cells(bank[best_index+1:], digits_required - 1)


def main():
    banks = format_input('input.txt')
    results = [int(find_largest_cells(bank)) for bank in banks]

    print("Sum of largest cells:", sum(results))


if __name__ == "__main__":
    main()
