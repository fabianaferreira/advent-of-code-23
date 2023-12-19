import re
from util import get_quantity_of_solutions, solve_equation

def get_numbers_from_line(line):
    numbers = re.findall(r"(\d+)", line)
    return [int(x) for x in numbers]

with open("input.txt", "r") as f:
    lines = f.readlines()
    product = 1
    # I know the file has only two lines, so I'm not iterating over them
    time = lines[0]
    distance = lines[1]
    time_numbers = get_numbers_from_line(time)
    distance_numbers = get_numbers_from_line(distance)
    for index, distance in enumerate(distance_numbers):
        limit1, limit2 = solve_equation(distance, time_numbers[index])
        product *= get_quantity_of_solutions(limit1, limit2)

print("Total product: ", product)
