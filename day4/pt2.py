from pathlib import Path
import sys

path_root = Path(__file__).parents[1]
sys.path.append(str(path_root))

from util import get_card_lists
from utils.sort import merge_sort
from utils.search import binary_search


def get_card_matches(winners, my_numbers):
    matches = 0
    for winner in winners:
        if binary_search(my_numbers, 0, len(my_numbers) - 1, winner) != -1:
            matches += 1
    return matches


with open("input.txt", "r") as f:
    lines = f.readlines()
    sum = 0
    sum_list = [1] * len(lines)
    copies = {}
    for index, line in enumerate(lines):
        winners_list, my_numbers_list = get_card_lists(line)
        merge_sort(my_numbers_list)
        matches = get_card_matches(winners_list, my_numbers_list)

        # Given the #matches, we're looping over the next
        # X indexes, where X is #matches. If the number of matches
        # goes beyond the table limit, we're iterating until the end of it
        if matches > 0:
            limit = min(index + matches + 1, len(lines))
            for match in range(index + 1, limit):
                sum_list[match] += sum_list[index]

        sum += sum_list[index]

print("Total sum:", sum)
