import re
from collections import namedtuple
from itertools import cycle


LR = namedtuple("LR", ["L", "R"])


def get_node_and_children(line):
    return re.findall(r"(\w+)\s=\s\((\w+),\s(\w+)\)", line)[0]


with open("input.txt", "r") as f:
    lines = f.readlines()
    route = ""
    nodes = {}
    steps = 0
    current_node = "AAA"
    for index, line in enumerate(lines):
        if index == 0:
            route = line
        elif index > 1:
            node, left, right = get_node_and_children(line)
            nodes[node] = LR(left, right)

    for direction in cycle(route.strip()):
        steps += 1
        if direction == "L":
            next_node = nodes[current_node].L
        else:
            next_node = nodes[current_node].R

        current_node = next_node
        if current_node == "ZZZ":
            print("Steps:", steps)
            break
