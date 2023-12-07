import re


def process_line(line):
    game, cubes = line.split(":")
    cubes_per_round = re.split(";|,", cubes.strip())
    return game, cubes_per_round
