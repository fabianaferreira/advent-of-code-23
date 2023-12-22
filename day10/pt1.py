from pathlib import Path
import sys

path_root = Path(__file__).parents[1]
sys.path.append(str(path_root))

from utils.search import bfs
from util import get_maze

N, S, E, W = -1, +1, +1j, -1j
directions = {
    "|": (N, S),
    "-": (E, W),
    "L": (N, E),
    "J": (N, W),
    "7": (S, W),
    "F": (S, E),
    "S": (N, E, S, W),
    ".": (),
}

valid_directions = {
    N: ("|", "7", "F", "S"),
    S: ("|", "L", "J", "S"),
    E: ("-", "J", "7", "S"),
    W: ("-", "L", "F", "S"),
}

maze, boundaries, start = get_maze()

graph = {}
# Build graph with all the possible directions per
# position in grid, and find the starting position
for position, character in maze.items():
    if character == ".":  # Floors are not nodes
        continue
    inner_set = set()
    for direction in directions[character]:
        dest_position = position + direction
        # We're only adding the possible directions that lay
        # within the maze boundaries
        if (
            0 <= dest_position.imag < boundaries[1]
            and 0 <= dest_position.real < boundaries[0]
        ):
            if (
                maze[dest_position] not in valid_directions[direction]
                or maze[dest_position] == "."
            ):
                continue
            inner_set.add(dest_position)
    graph[position] = inner_set

print("Max distance:", bfs(graph, start))
