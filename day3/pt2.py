import re


# Get all indexes in a line that is a symbol
def getSymbolsPositions(line):
    positions = []
    for match in re.finditer(r"[^\d.]", line):
        positions.append(match.start())
    return positions


def getFullFromFirstNumericPos(line, pos, direction):
    pointer = pos
    number = ""

    while line[pointer].isnumeric() and pointer >= 0 and pointer < len(line):
        number = number + line[pointer] if direction == 1 else line[pointer] + number
        pointer += 1 * direction

    return number


def getNumbersWhenCentralIsNumeric(line, pos):
    rightNumber = ""
    leftNumber = ""
    if pos + 1 < len(line):
        if line[pos + 1].isnumeric():
            rightNumber = getFullFromFirstNumericPos(line, pos, 1)
    if pos - 1 >= 0:
        if line[pos - 1].isnumeric():
            leftNumber = getFullFromFirstNumericPos(line, pos, -1)

    if rightNumber == "" and leftNumber == "":
        return int(line[pos])
    if leftNumber != "" and rightNumber != "":
        return int(leftNumber[:-1] + rightNumber)
    return int(leftNumber + rightNumber)


def getAdjacentNumbers(lineIndex, positions, lines):
    sum = 0

    for pos in positions:
        adjacentCount = 0
        product = 1
        # Check first the numbers in the same line
        if 0 <= pos + 1 < len(line) and lines[lineIndex][pos + 1].isnumeric():
            # From left to right
            adjacentCount += 1
            product *= int(getFullFromFirstNumericPos(line, pos + 1, 1))
            if adjacentCount == 2:
                sum += product
                continue
        if 0 <= pos - 1 < len(line) and lines[lineIndex][pos - 1].isnumeric():
            # From right to left
            adjacentCount += 1
            product *= int(getFullFromFirstNumericPos(line, pos - 1, -1))
            if adjacentCount == 2:
                sum += product
                continue
        # Check numbers from previous line
        if lineIndex > 0:
            previousLine = lines[lineIndex - 1]
            if 0 <= pos < len(previousLine) and previousLine[pos].isnumeric():
                adjacentCount += 1
                product *= getNumbersWhenCentralIsNumeric(previousLine, pos)
                if adjacentCount == 2:
                    sum += product
                    continue
            else:
                # Get numbers if central position is not a numeric value
                if (
                    0 <= pos - 1 < len(previousLine)
                    and previousLine[pos - 1].isnumeric()
                ):
                    adjacentCount += 1
                    product *= int(
                            getFullFromFirstNumericPos(previousLine, pos - 1, -1)
                        )
                    if adjacentCount == 2:
                        sum += product
                        continue
                if (
                    0 <= pos + 1 < len(previousLine)
                    and previousLine[pos + 1].isnumeric()
                ):
                    adjacentCount += 1
                    product *= int(
                            getFullFromFirstNumericPos(previousLine, pos + 1, 1)
                        )
                    if adjacentCount == 2:
                        sum += product
                        continue

        # Check numbers from next line
        if lineIndex < len(lines) - 1:
            nextLine = lines[lineIndex + 1]
            if 0 <= pos < len(nextLine) and nextLine[pos].isnumeric():
                adjacentCount += 1
                product *= getNumbersWhenCentralIsNumeric(nextLine, pos)
                if adjacentCount == 2:
                    sum += product
                    continue
            else:
                # Get numbers if central position is not a numeric value
                if 0 <= pos - 1 < len(nextLine) and nextLine[pos - 1].isnumeric():
                    adjacentCount += 1
                    product *= int(
                            getFullFromFirstNumericPos(nextLine, pos - 1, -1)
                        )
                    if adjacentCount == 2:
                        sum += product
                        continue
                if 0 <= pos + 1 < len(nextLine) and nextLine[pos + 1].isnumeric():
                    adjacentCount += 1
                    product *= int(getFullFromFirstNumericPos(nextLine, pos + 1, 1))
                    if adjacentCount == 2:
                        sum += product
                        continue
    return sum


with open("input.txt", "r") as f:
    lines = f.readlines()
    sum = 0
    for index, line in enumerate(lines):
        positions = getSymbolsPositions(line.strip())
        sum += getAdjacentNumbers(index, positions, lines)

print("Total sum: ", sum)
