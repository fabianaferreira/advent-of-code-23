import re

LIMITS = { "red": 12, "green": 13, "blue": 14 }
def processLine(line):
    game, cubes = line.split(":")
    cubesPerRound = re.split(";|,", cubes.strip())
    return game, cubesPerRound

def isGameValid(cubesPerRound):
    for cube in cubesPerRound:
        cube = cube.strip()
        qnt, color = cube.split(" ")
        if int(qnt) > LIMITS.get(color, 0):
            return False

    return True

with open("input.txt", "r") as f:
    lines = f.readlines()
    sum = 0
    for line in lines:
        game, rounds = processLine(line)
        if isGameValid(rounds):
            _, id = game.split(" ")
            sum += int(id)

print("Total sum: ", sum)