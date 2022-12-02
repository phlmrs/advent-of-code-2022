def p1(inp):
    return 0


def p2(inp):
    return 0


points = {
    'X': 1,
    'Y': 2,
    'Z': 3
}

p1_dict = {
    ('X', 'A'): 3,
    ('X', 'B'): 0,
    ('X', 'C'): 6,
    ('Y', 'A'): 6,
    ('Y', 'B'): 3,
    ('Y', 'C'): 0,
    ('Z', 'A'): 0,
    ('Z', 'B'): 6,
    ('Z', 'C'): 3,
}

p2_dict = {
    ('A', 'X'): 3, #lose
    ('B', 'X'): 1,
    ('C', 'X'): 2,
    ('A', 'Y'): 4, #draw
    ('B', 'Y'): 5,
    ('C', 'Y'): 6,
    ('A', 'Z'): 8, #win
    ('B', 'Z'): 9,
    ('C', 'Z'): 7,
}

with open('../../input/week1/day2.txt') as file:
    #sum = 0
    #for line in file:
    #    (opponent, you) = line.strip().split(' ')
    #    sum += points[you] + p1_dict[(you, opponent)]
    #print(sum)

    sum = 0
    for line in file:
        (opponent, you) = line.strip().split(' ')
        print(you, opponent)
        sum += p2_dict[(opponent, you)]
    print(sum)

    print('part 1: {}'.format(p1([])))
    print('part 2: {}'.format(p2([])))
