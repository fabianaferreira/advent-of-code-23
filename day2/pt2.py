import re

LIMITS = { "red": 12, "green": 13, "blue": 14 }
def processLine(line):
    game, cubes = line.split(":")
    cubesPerRound = re.split(";|,", cubes.strip())
    return game, cubesPerRound

def getPowerResult(cubesPerRound):
    plays = {}
    for cube in cubesPerRound:
        cube = cube.strip()
        qnt, color = cube.split(" ")
        currentValue = plays.get(color, 0)
        if currentValue == 0:
            plays[color] = int(qnt)
        else:
            if currentValue < int(qnt):
                plays[color] = int(qnt)

    maxPerColor = plays.values()
    power = 1
    for max in maxPerColor:
        power = power*max
    return power

with open("input.txt", "r") as f:
    lines = f.readlines()
    sum = 0
    for line in lines:
        game, rounds = processLine(line)
        sum += getPowerResult(rounds)

print("Total sum: ", sum)