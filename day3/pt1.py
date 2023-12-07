from util import (
    get_full_from_first_numeric_pos,
    get_symbols_positions,
    get_numbers_when_central_is_numeric,
)


def get_sum_from_different_line(pos, line):
    partial_sum = 0
    if 0 <= pos < len(line) and line[pos].isnumeric():
        partial_sum += get_numbers_when_central_is_numeric(line, pos)
    else:
        # Get numbers if central position is not a numeric value
        if 0 <= pos - 1 < len(line) and line[pos - 1].isnumeric():
            partial_sum += int(get_full_from_first_numeric_pos(line, pos - 1, -1))
        if 0 <= pos + 1 < len(line) and line[pos + 1].isnumeric():
            partial_sum += int(get_full_from_first_numeric_pos(line, pos + 1, 1))
    return partial_sum


def get_adjacent_numbers(index, positions, lines):
    partial_sum = 0
    for pos in positions:
        # Check first the numbers in the same line
        if 0 <= pos + 1 < len(line) and lines[index][pos + 1].isnumeric():
            # From left to right
            partial_sum += int(get_full_from_first_numeric_pos(line, pos + 1, 1))
        if 0 <= pos - 1 < len(line) and lines[index][pos - 1].isnumeric():
            # From right to left
            partial_sum += int(get_full_from_first_numeric_pos(line, pos - 1, -1))

        # Check numbers from previous line
        if index > 0:
            partial_sum += get_sum_from_different_line(pos, lines[index - 1])

        # Check numbers from next line
        if index < len(lines) - 1:
            partial_sum += get_sum_from_different_line(pos, lines[index + 1])

    return partial_sum


with open("input.txt", "r") as f:
    lines = f.readlines()
    sum = 0
    for index, line in enumerate(lines):
        positions = get_symbols_positions(line.strip())
        sum += get_adjacent_numbers(index, positions, lines)

print("Total sum: ", sum)
