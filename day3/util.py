import re

# Get all indexes in a line that is a symbol
def get_symbols_positions(line):
    positions = []
    for match in re.finditer(r"[^\d.]", line):
        positions.append(match.start())
    return positions


def get_full_from_first_numeric_pos(line, pos, direction):
    pointer = pos
    number = ""

    while line[pointer].isnumeric() and pointer >= 0 and pointer < len(line):
        number = number + line[pointer] if direction == 1 else line[pointer] + number
        pointer += 1 * direction

    return number


def get_numbers_when_central_is_numeric(line, pos):
    rightNumber = ""
    leftNumber = ""
    if pos + 1 < len(line):
        if line[pos + 1].isnumeric():
            rightNumber = get_full_from_first_numeric_pos(line, pos, 1)
    if pos - 1 >= 0:
        if line[pos - 1].isnumeric():
            leftNumber = get_full_from_first_numeric_pos(line, pos, -1)

    if rightNumber == "" and leftNumber == "":
        return int(line[pos])
    if leftNumber != "" and rightNumber != "":
        return int(leftNumber[:-1] + rightNumber)
    return int(leftNumber + rightNumber)
