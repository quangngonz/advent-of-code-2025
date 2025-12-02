
def format_input(file_path):
    with open(file_path, 'r') as file:
        lines = file.read().splitlines()

    formatted_lines = [line.strip().upper() for line in lines if line.strip()]
    formatted_instructions = [(i[0], int(i[1:])) for i in formatted_lines]

    # print(formatted_instructions)

    return formatted_instructions


def main():
    DIAL_NO = [i for i in range(100)]
    initial_pos = 50

    INPUT_FILE = 'input_1.txt'

    instructions = format_input(INPUT_FILE)

    password = 0

    for direction, steps in instructions:
        if direction == 'R':
            new_pos = (initial_pos + steps) % len(DIAL_NO)
        elif direction == 'L':
            new_pos = (initial_pos - steps) % len(DIAL_NO)

        if new_pos == 0:
            password += 1

        initial_pos = new_pos

    print(f"Final password: {password}")


if __name__ == "__main__":
    main()
