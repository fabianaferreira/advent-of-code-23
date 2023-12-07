from pathlib import Path
import sys
import re

path_root = Path(__file__).parents[1]
sys.path.append(str(path_root))

from utils.sort import mergeSort
from utils.search import binarySearch

# Sort the target array
# Loop over the numbers we have
# Use binary search to find the numbers that are in both
# O((N + M)logM)

# Get all indexes in a line that is a symbol
def getCardIdAndLists(line):
    (id, winnersStr, myNumbersStr) = re.findall(r"(\d):(.*)\|(.*)", line)[0]
    winnersList = winnersStr.strip().split()
    myNumbersList = myNumbersStr.strip().split()

    # Converting to int before returning the values
    winnersList = [int(x) for x in winnersList]
    myNumbersList = [int(x) for x in myNumbersList]

    return id, winnersList, myNumbersList


def getCardPoints(winners, myNumbers):
    matches = 0
    for winner in winners:
        if binarySearch(myNumbers, 0, len(myNumbers) - 1, winner) != -1:
            matches += 1
    
    return 2**(matches - 1) if matches > 0 else 0

with open("input.txt", "r") as f:
    lines = f.readlines()
    sum = 0
    for index, line in enumerate(lines):
        id, winnerList, myNumbersList = getCardIdAndLists(line)
        mergeSort(myNumbersList)
        sum += getCardPoints(winnerList, myNumbersList)

print("Total sum:", sum)
