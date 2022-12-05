import re


def p1(stacks_str, instructions_str):
    stacks = get_stacks(stacks_str)
    instructions_str_lines = instructions_str.split('\n')

    for instructions_str_line in instructions_str_lines:
        (count, src, dest) = [int(num) for num in re.findall(r'\d+', instructions_str_line)]
        for i in range(count):
            stacks[dest].append(stacks[src].pop())

    return get_result(stacks)


def p2(stacks_str, instructions_str):
    stacks = get_stacks(stacks_str)
    instructions_str_lines = instructions_str.split('\n')

    for instructions_str_line in instructions_str_lines:
        (count, src, dest) = [int(num) for num in re.findall(r'\d+', instructions_str_line)]
        for crate in stacks[src][-count:]:
            stacks[dest].append(crate)
        stacks[src] = stacks[src][:len(stacks[src]) - count]

    return get_result(stacks)


def get_stacks(stacks_str):
    stacks_str_lines = stacks_str.split('\n')
    stack_count = (len(stacks_str_lines[-1]) + 2) // 4
    stacks = {i: [] for i in range(1, stack_count + 1)}

    for stacks_str_line in stacks_str_lines[-2::-1]:
        for i in range(1, len(stacks_str_line), 4):
            if stacks_str_line[i] != ' ':
                stacks[(i + 3) // 4].append(stacks_str_line[i])

    return stacks


def get_result(stacks):
    res = ''
    for stack in stacks.values():
        res += stack[-1]
    return res


with open('../../input/week1/day5.txt') as file:
    (top_inp, bottom_inp) = file.read().split('\n\n')

    print('part 1: {}'.format(p1(top_inp, bottom_inp)))
    print('part 2: {}'.format(p2(top_inp, bottom_inp)))
