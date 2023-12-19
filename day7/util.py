import re


def get_card_and_bid(line):
    return re.findall(r"(.*)\s(\d+)", line)[0]


def remap_chars_from_card(card, mask):
    transform = str.maketrans("TJQKA", mask)

    return str.translate(card, transform)
