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
            print(sub_folder, filesystem[sub_folder], item)
            folder_size += get_subfolder_size(item)
    filesystem[sub_folder] = [folder_size]
    return folder_size


with open('../../input/week1/day7.txt') as file:
    # TODO directories können den gleichen Namen haben
    filesystem = {}
    current_dir = ''
    for line in file.readlines():
        cmd = line.strip().split(' ')
        if cmd[1] == 'cd':
            if cmd[2] == '..':
                continue
            if cmd[2] not in filesystem:
                filesystem[cmd[2]] = []
            current_dir = cmd[2]
        elif cmd[1] == 'ls':
            continue
        elif cmd[0] == 'dir':
            if cmd[1] not in filesystem[current_dir] and cmd[1] != current_dir:
                filesystem[current_dir].append(cmd[1])
        elif cmd[0].isalnum():
            filesystem[current_dir].append(int(cmd[0]))

    print(filesystem)

    for folder in filesystem:
        folder_size = 0
        for item in filesystem[folder]:
            if isinstance(item, int):
                folder_size += item
            else:
                print(folder, filesystem[folder], item)
                folder_size += get_subfolder_size(item)
        filesystem[folder] = [folder_size]

    res = 0
    for folder_size in filesystem.values():
        if folder_size[0] <= 100000:
            res += folder_size[0]
    print(filesystem)
    print(res)

    print('part 1: {}'.format(p1([])))
    print('part 2: {}'.format(p2([])))
