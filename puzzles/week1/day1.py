def p1(inp):
    temp = 0
    maximum = 0

    for line in inp:
        if line != '':
            temp += int(line)
        else:
            if temp > maximum:
                maximum = temp
            temp = 0
    if temp > maximum:
        maximum = temp

    return maximum


def p2(inp):
    temp = 0
    calories = []

    for line in inp:
        if line != '':
            temp += int(line)
        else:
            calories.append(temp)
            temp = 0

    calories.append(temp)
    ordered = sorted(calories)

    return ordered[-1] + ordered[-2] + ordered[-3]


with open('../../input/week1/day1.txt') as file:
    inp = []
    for line in file:
        inp.append(line.strip())

    print('part 1: {}'.format(p1(inp)))
    print('part 2: {}'.format(p2(inp)))
