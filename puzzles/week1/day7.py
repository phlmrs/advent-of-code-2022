def p1(inp):
    res = 0
    for folder_size in inp.values():
        if folder_size[0] <= 100000:
            res += folder_size[0]
    return res


def p2(inp):
    to_clear = 30000000 - (70000000 - inp['/'][0])
    delete_candidates = []
    for folder_size in inp.values():
        if folder_size[0] >= to_clear:
            delete_candidates.append(folder_size[0])
    return min(delete_candidates)


def get_subfolder_size(sub_folder):
    folder_size = 0
    for item in filesystem[sub_folder]:
        if isinstance(item, int):
            folder_size += item
        else:
            folder_size += get_subfolder_size(item)
    filesystem[sub_folder] = [folder_size]
    return folder_size


def get_parent(folder_path):
    history = folder_path.split('_')
    res = ''
    for item in history[:-1]:
        res = res + item + '_'
    return res.rstrip('_')


with open('../../input/week1/day7.txt') as file:
    filesystem = {'/': []}
    current_path = ''

    for line in file.readlines():
        cmd = line.strip().split(' ')

        if cmd[1] == 'cd':
            if current_path == '':
                current_path = '/'
                continue
            if cmd[2] == '..':
                current_path = get_parent(current_path)
                continue

            new_path = current_path + '_' + cmd[2]
            if new_path not in filesystem:
                filesystem[new_path] = []
            current_path = new_path

        elif cmd[1] == 'ls':
            continue

        elif cmd[0] == 'dir':
            new_path = current_path + '_' + cmd[1]
            if new_path not in filesystem[current_path]:
                filesystem[current_path].append(new_path)

        elif cmd[0].isalnum():
            filesystem[current_path].append(int(cmd[0]))

    for folder in filesystem:
        folder_size = 0
        for item in filesystem[folder]:
            if isinstance(item, int):
                folder_size += item
            else:
                folder_size += get_subfolder_size(item)
        filesystem[folder] = [folder_size]

    print('part 1: {}'.format(p1(filesystem)))
    print('part 2: {}'.format(p2(filesystem)))
