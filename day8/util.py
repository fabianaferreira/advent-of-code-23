from itertools import cycle
import re


def get_node_and_children(line):
    return re.findall(r"(\w+)\s=\s\((\w+),\s(\w+)\)", line)[0]


def calculate_steps(route, nodes, initial_node):
    steps = 0
    current_node = initial_node
    for direction in cycle(route.strip()):
        steps += 1
        if direction == "L":
            next_node = nodes[current_node].L
        else:
            next_node = nodes[current_node].R

        current_node = next_node
        if current_node.endswith("Z"):
            break

    return steps
