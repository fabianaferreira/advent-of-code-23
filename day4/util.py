import re


# Get all indexes in a line that is a symbol
def get_card_lists(line):
    (winners_str, my_numbers_str) = re.findall(r"\d+:(.*)\|(.*)", line)[0]
    # Converting to int before returning the values
    winners_list = [int(x) for x in winners_str.strip().split()]
    my_numbers_list = [int(x) for x in my_numbers_str.strip().split()]

    return winners_list, my_numbers_list
