import re


def get_numbers_from_line(line):
    numbers = re.findall(r"(\-?\d+)", line)
    return [int(x) for x in numbers]


# Recursive function that iterates over a list of numbers
# and transform the list until all numbers are zero
def get_prediction(numbers, direction="forward"):
    last_numbers = [numbers[-1]] if direction == "forward" else [numbers[0]]
    current_values = numbers
    while not all(p == 0 for p in current_values):
        aux_list = []
        for index, number in enumerate(current_values):
            if index > 0:
                aux_list.append(number - current_values[index - 1])
        current_values = aux_list
        if current_values:  # Check if current_values is not empty
            last_numbers.append(
                current_values[-1] if direction == "forward" else current_values[0]
            )
    return last_numbers


def calculate_next_value(values, direction="forward"):
    value = 0
    while len(values) > 0:
        value = values.pop() + value if direction == "forward" else values.pop() - value
    return value
