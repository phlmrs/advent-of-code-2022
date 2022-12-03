def p1(inp):
    sum = 0
    for line in inp:
        intersec = set(line[:(len(line) // 2)]).intersection(set(line[(len(line) // 2):]))
        for item in intersec:
            sum += ord(item) - 38 if item.isupper() else ord(item) - 96
    return sum


def p2(inp):
    sum = 0
    for i in range(0, len(inp), 3):
        intersec = set(inp[i]).intersection(set(inp[i + 1])).intersection(set(inp[i + 2]))
        for item in intersec:
            sum += ord(item) - 38 if item.isupper() else ord(item) - 96

    return sum


with open('../../input/week1/day3.txt') as file:
    lines = file.read().strip().split('\n')

    print('part 1: {}'.format(p1(lines)))
    print('part 2: {}'.format(p2(lines)))
