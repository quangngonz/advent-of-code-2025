from task_1 import format_input


def check_product_id(product_id):
    s = str(product_id)
    if len(s) < 2:
        return False

    for pattern_len in range(1, len(s) // 2 + 1):
        if len(s) % pattern_len == 0:
            pattern = s[:pattern_len]
            if pattern * (len(s) // pattern_len) == s:
                return True

    return False


def main():
    invalid_ids = []

    product_id_ranges = format_input('input_1.txt')

    for start, end in product_id_ranges:
        for product_id in range(start, end + 1):
            if check_product_id(product_id):
                invalid_ids.append(product_id)

    print("Sum of invalid product IDs:", sum(invalid_ids))


if __name__ == "__main__":
    main()
