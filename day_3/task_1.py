
def format_input(filename):
    with open(filename, 'r') as file:
        lines = file.read().splitlines()

    # print(lines)

    return lines


def find_largest_cells(bank):
    first_digit = [0, bank[0]]
    second_digit = [0, bank[-1]]

    for i in range(1, len(bank)-1):
        if bank[i] > first_digit[1]:
            first_digit = [i, bank[i]]

    for j in range(first_digit[0]+1, len(bank)):
        if bank[j] > second_digit[1]:
            second_digit = [j, bank[j]]

    return int(first_digit[1] + second_digit[1])


def main():
    banks = format_input('input.txt')
    results = [find_largest_cells(bank) for bank in banks]

    print("Sum of indices:", sum(results))


if __name__ == "__main__":
    main()
