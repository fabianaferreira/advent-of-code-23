from pathlib import Path
import sys

path_root = Path(__file__).parents[1]
sys.path.append(str(path_root))

from util import get_card_lists
from utils.sort import merge_sort
from utils.search import binary_search

# Sort the target array
# Loop over the numbers we have
# Use binary search to find the numbers that are in both
# O((N + M)logM)


def get_card_points(winners, my_numbers):
    matches = 0
    for winner in winners:
        if binary_search(my_numbers, 0, len(my_numbers) - 1, winner) != -1:
            matches += 1

    return 2 ** (matches - 1) if matches > 0 else 0


with open("input.txt", "r") as f:
    lines = f.readlines()
    sum = 0
    for index, line in enumerate(lines):
        winners_list, my_numbers_list = get_card_lists(line)
        merge_sort(my_numbers_list)
        sum += get_card_points(winners_list, my_numbers_list)

print("Total sum:", sum)
