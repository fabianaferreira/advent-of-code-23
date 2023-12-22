def get_maze():
    maze = {}
    len_lines = len_columns = 0
    start = complex(0, 0)
    with open("input.txt", "r") as f:
        lines = f.readlines()
        len_lines = len(lines)
        for h_index, line in enumerate(lines):
            line = line.strip()
            len_columns = len(line)
            for v_index, character in enumerate(line):
                if character == "S":
                    start = complex(h_index, v_index)
                maze[complex(h_index, v_index)] = character

    return maze, (len_lines, len_columns), start
