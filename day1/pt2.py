import re

NUMBERS = { "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9 }

def processLine(line):
    numbers = re.findall(r"(?=(one|two|three|four|five|six|seven|eight|nine|\d))", line)
    numbers = [str(NUMBERS.get(x, x)) for x in numbers]
    return numbers[0] + numbers[-1]

with open("input.txt", "r") as f:
    lines = f.readlines()
    sum = 0
    for line in lines:
        lineNumber = processLine(line)
        print(lineNumber)
        sum += int(lineNumber)

print("Total in file: ", sum)