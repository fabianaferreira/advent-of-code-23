from collections import namedtuple
from util import calculate_steps, get_node_and_children
from math import lcm

LR = namedtuple("LR", ["L", "R"])


with open("input.txt", "r") as f:
    lines = f.readlines()
    route = ""
    nodes = {}
    start_nodes = []
    steps_per_start_node = []
    for index, line in enumerate(lines):
        if index == 0:
            route = line
        elif index > 1:
            node, left, right = get_node_and_children(line)
            if node[-1] == "A":
                start_nodes.append(node)
            nodes[node] = LR(left, right)

    for node in start_nodes:
        steps_per_start_node.append(calculate_steps(route, nodes, node))
        
    print(lcm(*steps_per_start_node))
