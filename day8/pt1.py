from collections import namedtuple
from util import calculate_steps, get_node_and_children


LR = namedtuple("LR", ["L", "R"])


with open("input.txt", "r") as f:
    lines = f.readlines()
    route = ""
    nodes = {}
    for index, line in enumerate(lines):
        if index == 0:
            route = line
        elif index > 1:
            node, left, right = get_node_and_children(line)
            nodes[node] = LR(left, right)

    print("Steps:", calculate_steps(route, nodes, "AAA"))
