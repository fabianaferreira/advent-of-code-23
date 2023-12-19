import re
from util import get_quantity_of_solutions, solve_equation


def get_concatenated_number(line):
    numbers = re.findall(r"(\d+)", line)
    return "".join(numbers)


with open("input.txt", "r") as f:
    lines = f.readlines()
    time = get_concatenated_number(lines[0])
    distance = get_concatenated_number(lines[1])
    limit1, limit2 = solve_equation(int(distance), int(time))


print("Total ways: ", get_quantity_of_solutions(limit1, limit2))
