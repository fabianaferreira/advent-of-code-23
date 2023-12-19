import re
import math


def get_numbers_from_line(line):
    numbers = re.findall(r"(\d+)", line)
    return [int(x) for x in numbers]


def solve_equation(distance, time):
    delta = time**2 - 4 * distance
    limit1 = (-time + delta**0.5) / 2
    limit2 = (-time - delta**0.5) / 2

    return math.ceil(limit1), math.floor(limit2)


def get_quantity_of_solutions(limit1, limit2):
    if limit1 == limit2:
        return 1
    return limit2 - limit1 + 1


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
