from util import get_prediction, get_numbers_from_line, calculate_next_value

with open("input.txt", "r") as f:
    lines = f.readlines()
    total = 0
    for line in lines:
        numbers = get_numbers_from_line(line)
        last_numbers = get_prediction(numbers)
        total += calculate_next_value(last_numbers)

    print("Total sum:", total)
