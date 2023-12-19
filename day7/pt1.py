from util import get_card_and_bid, remap_chars_from_card


def map_card_to_strength(card):
    chars_map = {}
    for char in card:
        if chars_map.get(char, -1) == -1:
            chars_map[char] = 1
        else:
            chars_map[char] += 1

    type_list = [str(x) for x in sorted(chars_map.values(), reverse=True)]

    return "".join(type_list)


with open("input.txt", "r") as f:
    lines = f.readlines()
    card_rank_list = []
    sum = 0
    for line in lines:
        card, bid = get_card_and_bid(line)
        # Create a list of tuples with the card, its strength and its bid
        card_rank_list.append(
            (remap_chars_from_card(card, "ABCDE"), map_card_to_strength(card), int(bid))
        )

    sorted_card_rank = sorted(card_rank_list, key=lambda x: (x[1], x[0]))
    for index, tup in enumerate(sorted_card_rank):
        sum += (index + 1) * tup[2]

print("Total sum: ", sum)
