def get_input(fn):
    dirs = []
    with open(fn, 'r') as f:
        for l in f.readline():
            l = l.replace('\n','')
            for c in l:
                dirs.append(c)

    return dirs

def p1(dirs):
    tracker = {}
    pos = [0, 0]
    tracker[tuple(pos)] = 1

    for d in dirs:
        if d == '^':
            pos[1] += 1
        elif d == '>':
            pos[0] += 1
        elif d == '<':
            pos[0] -= 1
        elif d == 'v':
            pos[1] -= 1

        if tuple(pos) not in tracker:
            tracker[tuple(pos)] = 1
        else:
            tracker[tuple(pos)] += 1

    print('part 1:', len(tracker))

def p2(dirs):
    tracker = {}
    s, rs = [0, 0], [0, 0]
    
    tracker[tuple(s)] = 2

    def increment(pos, d):
        if d == '^':
            pos[1] += 1
        elif d == '>':
            pos[0] += 1
        elif d == '<':
            pos[0] -= 1
        elif d == 'v':
            pos[1] -= 1

        if tuple(pos) not in tracker:
            tracker[tuple(pos)] = 1
        else:
            tracker[tuple(pos)] += 1

        return pos

    for i in range(0, len(dirs), 2):
        s = increment(s, dirs[i])

    for i in range(1, len(dirs), 2):
        rs = increment(rs, dirs[i])

    print('part 2:', len(tracker))

def sol(dirs):
    p1(dirs)
    p2(dirs)
    
if __name__ == '__main__':
    dirs = get_input('input.txt')
    # dirs = get_input('test.txt')
    sol(dirs)