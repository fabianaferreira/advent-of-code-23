from util import (
    get_full_from_first_numeric_pos,
    get_symbols_positions,
    get_numbers_when_central_is_numeric,
)


# Returns if the adjacent count reached its max, and the partial sum
def get_sum_from_different_line(pos, line, current_product, adjacent_count):
    partial_product = current_product

    if 0 <= pos < len(line) and line[pos].isnumeric():
        adjacent_count += 1
        partial_product *= get_numbers_when_central_is_numeric(line, pos)
        if adjacent_count == 2:
            return adjacent_count, partial_product
    else:
        # Get numbers if central position is not a numeric value
        if 0 <= pos - 1 < len(line) and line[pos - 1].isnumeric():
            adjacent_count += 1
            partial_product *= int(get_full_from_first_numeric_pos(line, pos - 1, -1))
            if adjacent_count == 2:
                return adjacent_count, partial_product
        if 0 <= pos + 1 < len(line) and line[pos + 1].isnumeric():
            adjacent_count += 1
            partial_product *= int(get_full_from_first_numeric_pos(line, pos + 1, 1))
            if adjacent_count == 2:
                return adjacent_count, partial_product

    return adjacent_count, partial_product


def get_adjacent_numbers(index, positions, lines):
    sum = 0

    for pos in positions:
        adjacent_count = 0
        product = 1
        # Check first the numbers in the same line
        if 0 <= pos + 1 < len(line) and lines[index][pos + 1].isnumeric():
            # From left to right
            adjacent_count += 1
            product *= int(get_full_from_first_numeric_pos(line, pos + 1, 1))
            if adjacent_count == 2:
                sum += product
                continue
        if 0 <= pos - 1 < len(line) and lines[index][pos - 1].isnumeric():
            # From right to left
            adjacent_count += 1
            product *= int(get_full_from_first_numeric_pos(line, pos - 1, -1))
            if adjacent_count == 2:
                sum += product
                continue
        # Check numbers from previous line
        if index > 0:
            updated_count, updated_product = get_sum_from_different_line(
                pos, lines[index - 1], product, adjacent_count
            )
            if updated_count == 2:
                sum += updated_product
                continue
            product = updated_product
            adjacent_count = updated_count

        # Check numbers from next line
        if index < len(lines) - 1:
            updated_count, updated_product = get_sum_from_different_line(
                pos, lines[index + 1], product, adjacent_count
            )
            if updated_count == 2:
                sum += updated_product
                continue
            product = updated_product
            adjacent_count = updated_count
    return sum


with open("input.txt", "r") as f:
    lines = f.readlines()
    sum = 0
    for index, line in enumerate(lines):
        positions = get_symbols_positions(line.strip())
        sum += get_adjacent_numbers(index, positions, lines)

print("Total sum: ", sum)
