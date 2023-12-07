from util import process_line

LIMITS = {"red": 12, "green": 13, "blue": 14}


def is_game_valid(cubes_per_round):
    for cube in cubes_per_round:
        cube = cube.strip()
        qnt, color = cube.split(" ")
        if int(qnt) > LIMITS.get(color, 0):
            return False

    return True


with open("input.txt", "r") as f:
    lines = f.readlines()
    sum = 0
    for line in lines:
        game, rounds = process_line(line)
        if is_game_valid(rounds):
            _, id = game.split(" ")
            sum += int(id)

print("Total sum: ", sum)
