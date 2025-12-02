from task_1 import format_input


def roate_dial(current_pos, direction, steps, dial_length):
    no_zeros = 0

    for _ in range(steps):
        if direction == 'R':
            current_pos = (current_pos + 1) % dial_length
        elif direction == 'L':
            current_pos = (current_pos - 1) % dial_length

        if current_pos == 0:
            no_zeros += 1

    return current_pos, no_zeros


def main():
    DIAL_NO = [i for i in range(100)]
    initial_pos = 50

    INPUT_FILE = 'input_1.txt'

    instructions = format_input(INPUT_FILE)

    password = 0

    for direction, steps in instructions:
        initial_pos, zeros = roate_dial(
            initial_pos, direction, steps, len(DIAL_NO))
        password += zeros

    print(f"Final password: {password}")


if __name__ == "__main__":
    main()
