def p1(inp):
    return 0


def p2(inp):
    return 0


def get_subfolder_size(sub_folder):
    folder_size = 0
    for item in filesystem[sub_folder]:
        if isinstance(item, int):
            folder_size += item
        else:
            folder_size += get_subfolder_size(item)
    filesystem[sub_folder] = [folder_size]
    return folder_size


with open('../../input/week1/day7.txt') as file:
    filesystem = {'/': []}
    current_dir = ''
    for line in file.readlines():
        cmd = line.strip().split(' ')
        if cmd[1] == 'cd':
            if cmd[2] == '..':
                history = current_dir.split('_')
                current_dir = ''
                for item in history[:-1]:
                    current_dir = current_dir + item + '_'
                current_dir = current_dir.rstrip('_')
                continue
            if current_dir == '':
                current_dir = '/'
                continue
            elif current_dir + '_' + cmd[2] not in filesystem:
                filesystem[current_dir + '_' + cmd[2]] = []
            current_dir = current_dir + '_' + cmd[2]
        elif cmd[1] == 'ls':
            continue
        elif cmd[0] == 'dir':
            if (current_dir + '_' + cmd[1]) not in filesystem[current_dir] and (current_dir + '_' + cmd[1]) != current_dir:
                filesystem[current_dir].append(current_dir + '_' + cmd[1])
        elif cmd[0].isalnum():
            filesystem[current_dir].append(int(cmd[0]))

    for folder in filesystem:
        folder_size = 0
        for item in filesystem[folder]:
            if isinstance(item, int):
                folder_size += item
            else:
                folder_size += get_subfolder_size(item)
        filesystem[folder] = [folder_size]

    res = 0
    for folder_size in filesystem.values():
        if folder_size[0] <= 100000:
            res += folder_size[0]

    print(res)

    print('part 1: {}'.format(p1([])))
    print('part 2: {}'.format(p2([])))
