import re

def processLine(line):
    numbers = re.findall(r"(?=(\d))", line)
    return numbers[0] + numbers[-1]

with open("input.txt", "r") as f:
    lines = f.readlines()
    sum = 0
    for line in lines:
        lineNumber = processLine(line)
        print(lineNumber)
        sum += int(lineNumber)

print("Total in file: ", sum)