import math

# th^2 - th*ttotal + d = 0
def solve_equation(distance, time):
    delta = time**2 - 4 * distance
    limit1 = (time - delta**0.5) / 2
    limit2 = (time + delta**0.5) / 2

    return math.ceil(limit1), math.floor(limit2)


def get_quantity_of_solutions(limit1, limit2):
    if limit1 == limit2:
        return 1
    return limit2 - limit1 + 1
