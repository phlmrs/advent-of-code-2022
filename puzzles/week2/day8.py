def p1(inp):
    sum = grid_height * grid_width

    for x in range(1, grid_width - 1):
        for y in range(1, grid_height - 1):
            visible_directions = 4
            if max([row[x] for row in inp[y + 1:grid_height]]) >= inp[y][x]:    # down
                visible_directions -= 1
            if max([row[x] for row in inp[0:y]]) >= inp[y][x]:                  # up
                visible_directions -= 1
            if max(inp[y][x + 1:grid_width]) >= inp[y][x]:                      # right
                visible_directions -= 1
            if max(inp[y][0:x]) >= inp[y][x]:                                   # left
                visible_directions -= 1
            if visible_directions == 0:
                sum -= 1
    return sum


def get_view_distance(curr_height, heights):
    res = 0
    for height in heights:
        res += 1
        if height >= curr_height:
            break
    return res


def p2(inp):
    res = 0

    for x in range(grid_width):
        for y in range(grid_height):
            scenic_score = 1
            scenic_score *= get_view_distance(inp[y][x], [row[x] for row in inp[y + 1:grid_height]])    # down
            scenic_score *= get_view_distance(inp[y][x], [row[x] for row in reversed(inp[0:y])])        # up
            scenic_score *= get_view_distance(inp[y][x], inp[y][x + 1:grid_width])                      # right
            scenic_score *= get_view_distance(inp[y][x], reversed(inp[y][0:x]))                         # left
            if scenic_score > res:
                res = scenic_score
    return res


with open('../../input/week2/day8.txt') as file:
    global grid_height, grid_width
    grid = []
    for line in file.readlines():
        row = [int(height) for height in line.strip()]
        grid.append(row)
    grid_height = len(grid)
    grid_width = len(grid[0])

    print('part 1: {}'.format(p1(grid)))
    print('part 2: {}'.format(p2(grid)))
