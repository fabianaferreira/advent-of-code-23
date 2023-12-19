from util import get_card_and_bid, remap_chars_from_card


def map_card_to_strength(card):
    chars_map = {}
    joker_count = 0

    for char in card:
        if char == "J":
            joker_count += 1
            continue
        if chars_map.get(char, -1) == -1:
            chars_map[char] = 1
        else:
            chars_map[char] += 1

    # Sort map by values
    sorted_chars = dict(sorted(chars_map.items(), key=lambda x: x[1], reverse=True))
    if joker_count == 5:
        return "5"
    first_key = next(iter(sorted_chars), -1)
    if first_key != -1:
        sorted_chars[first_key] += joker_count
    return "".join([str(x) for x in sorted_chars.values()])


with open("input.txt", "r") as f:
    lines = f.readlines()
    card_rank_list = []
    sum = 0
    for line in lines:
        card, bid = get_card_and_bid(line)
        # Create a list of tuples with the card, its strength and its bid
        card_rank_list.append(
            (remap_chars_from_card(card, "A1BCD"), map_card_to_strength(card), int(bid))
        )

    sorted_card_rank = sorted(card_rank_list, key=lambda x: (x[1], x[0]))
    for index, tup in enumerate(sorted_card_rank):
        sum += (index + 1) * tup[2]

print("Total sum: ", sum)
