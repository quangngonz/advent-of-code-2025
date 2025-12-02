
def format_input(filename):
    with open(filename, 'r') as file:
        data = file.read().split(',')

    product_id_ranges = [d.strip().split('-') for d in data if '-' in d]
    product_id_ranges = [(int(start), int(end))
                         for start, end in product_id_ranges]

    # print(f"Parsed product ID ranges: {product_id_ranges}")

    return product_id_ranges


def check_product_id(product_id):
    s = str(product_id)
    if len(s) < 2 or len(s) % 2 != 0:
        return False

    half = len(s) // 2
    return s[:half] == s[half:]


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
