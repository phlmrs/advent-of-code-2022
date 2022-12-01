def p1(inp):
    return max(inp)


def p2(inp):
    return sum(inp[-3:])


with open('../../input/week1/day1.txt') as file:
    line_tuples = file.read().split('\n\n')
    calorie_tuples = [line_tuple.strip().split('\n') for line_tuple in line_tuples]
    calorie_sums = []
    for calorie_tuple in calorie_tuples:
        calorie_sum = sum([int(calorie_count) for calorie_count in calorie_tuple])
        calorie_sums.append(calorie_sum)
    calorie_sums = sorted(calorie_sums)

    print('part 1: {}'.format(p1(calorie_sums)))
    print('part 2: {}'.format(p2(calorie_sums)))
