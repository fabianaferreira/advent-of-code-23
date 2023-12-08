import re
from collections import namedtuple

Range = namedtuple("Range", ["destination_start", "source_start", "interval"])


def get_seeds(line):
    return [int(x) for x in (re.findall(r"\w+:(.*)", line)[0].strip()).split()]


def get_range_from_line(line):
    return Range(
        *[int(x) for x in re.findall(r"(\d+\s\d+\s\d+)", line)[0].strip().split()]
    )


def get_category_if_exists(line):
    matches = re.findall(r"(\w+\-\w+\-\w+)\s\w+:", line)
    if len(matches) > 0:
        return matches[0]
    return ""


def get_dest_value(source_value, ranges):
    for range in ranges:
        if range.source_start <= source_value < range.source_start + range.interval:
            return range.destination_start + source_value - range.source_start

    return source_value


with open("input.txt", "r") as f:
    lines = f.readlines()
    sum = 0
    seeds = []
    category_map = {}
    need_to_get_ranges_from_category = False
    current_category = ""
    for index, line in enumerate(lines):
        # If we are in the first line, we need to get the
        # seeds numbers
        if index == 0:
            seeds = get_seeds(line)
        # If we have a category line, the next lines
        # will be the number mapping, so we have to
        # create an map entry to store those until
        # we get to an emtpy line
        category = get_category_if_exists(line)
        if category != "":
            category_map[category] = category_map.get(category, [])
            need_to_get_ranges_from_category = True
            current_category = category
            continue
        if need_to_get_ranges_from_category and line != "\n":
            category_map[current_category].append(get_range_from_line(line))
            continue
    lowest_location = None
    for seed in seeds:
        current_value = seed
        for category, ranges in category_map.items():
            current_value = get_dest_value(current_value, ranges)
        if lowest_location == None or current_value < lowest_location:
            lowest_location = current_value

print(lowest_location)