def p1(inp):
    return find_marker_pos(inp, 4)


def p2(inp):
    return find_marker_pos(inp, 14)


def find_marker_pos(data, markerLen):
    for i in range(len(data) - markerLen - 1):
        if len(set(data[i:i + markerLen])) == markerLen:
            return i + markerLen
    return -1


with open('../../input/week1/day6.txt') as file:
    data = file.read()

    print('part 1: {}'.format(p1(data)))
    print('part 2: {}'.format(p2(data)))
