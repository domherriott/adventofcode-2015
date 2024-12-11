def get_input(fn):
    presents = []
    with open(fn, 'r') as f:
        for line in f.readlines():
            dims = line.replace('\n','').split('x')
            presents.append(sorted([int(d) for d in dims]))

    return presents

def sol(presents):
    wp, rb = 0, 0
    for present in presents:
        l, w, h = present
        wp += ((3*l*w) + (2*w*h) + (2*h*l))
        rb += (2*(l+w)) + (l*w*h)

    print('part 1:', wp)
    print('part 2:', rb)

if __name__ == '__main__':
    presents = get_input('input.txt')
    sol(presents)