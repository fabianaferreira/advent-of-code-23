import re


def process_line(line):
    numbers = re.findall(r"(?=(\d))", line)
    return str(numbers[0]) + str(numbers[-1])


with open("input.txt", "r") as f:
    lines = f.readlines()
    sum = 0
    for line in lines:
        line_number = process_line(line)
        sum += int(line_number)

print("Total in file: ", sum)
