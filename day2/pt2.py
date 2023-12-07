from util import process_line

LIMITS = {"red": 12, "green": 13, "blue": 14}


def get_power_result(cubes_per_round):
    plays = {}
    for cube in cubes_per_round:
        cube = cube.strip()
        qnt, color = cube.split(" ")
        current = plays.get(color, 0)
        if current == 0:
            plays[color] = int(qnt)
        else:
            if current < int(qnt):
                plays[color] = int(qnt)

    max_per_color = plays.values()
    power = 1
    for max in max_per_color:
        power = power * max
    return power


with open("input.txt", "r") as f:
    lines = f.readlines()
    sum = 0
    for line in lines:
        game, rounds = process_line(line)
        sum += get_power_result(rounds)

print("Total sum: ", sum)
