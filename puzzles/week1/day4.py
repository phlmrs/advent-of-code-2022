def p1(inp):
    res = 0
    for line in inp:
        (first, second) = line.split(',')
        first = [int(section) for section in first.split('-')]
        second = [int(section) for section in second.split('-')]
        if first[0] >= second[0] and first[1] <= second[1] or second[0] >= first[0] and second[1] <= first[1]:
            res += 1
    return res


def p2(inp):
    res = 0
    for line in inp:
        (first, second) = line.split(',')
        first = [int(section) for section in first.split('-')]
        second = [int(section) for section in second.split('-')]
        if first[0] <= second[0] <= first[1] or second[0] <= first[0] <= second[1]:
            res += 1
    return res


with open('../../input/week1/day4.txt') as file:
    lines = file.read().strip().split('\n')

    print('part 1: {}'.format(p1(lines)))
    print('part 2: {}'.format(p2(lines)))
