def p1(inp):
    # (what the opponent plays, what you should play): the score
    p1_dict = {
        ('A', 'X'): 4,
        ('B', 'X'): 1,
        ('C', 'X'): 7,
        ('A', 'Y'): 8,
        ('B', 'Y'): 5,
        ('C', 'Y'): 2,
        ('A', 'Z'): 3,
        ('B', 'Z'): 9,
        ('C', 'Z'): 6,
    }

    return sum([p1_dict[(opponent, result)] for opponent, result in inp])


def p2(inp):
    # (what the opponent plays, how the round ends): the score
    p2_dict = {
        ('A', 'X'): 3,
        ('B', 'X'): 1,
        ('C', 'X'): 2,
        ('A', 'Y'): 4,
        ('B', 'Y'): 5,
        ('C', 'Y'): 6,
        ('A', 'Z'): 8,
        ('B', 'Z'): 9,
        ('C', 'Z'): 7,
    }

    return sum([p2_dict[(opponent, result)] for opponent, result in inp])


with open('../../input/week1/day2.txt') as file:
    guides = []
    for line in file:
        (first, second) = line.strip().split(' ')
        guides.append((first, second))

    print('part 1: {}'.format(p1(guides)))
    print('part 2: {}'.format(p2(guides)))
