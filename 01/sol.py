def get_input(fn):
    with open(fn, 'r') as f:
        floors = f.readline()

    return floors

def sol(floors):
    floor = floors.count('(') - floors.count(')')
    print('p1:', floor)

    floor_num = 0
    for i, c in enumerate(floors):
        if c == '(':
            floor_num += 1
        else:
            floor_num -= 1

        if floor_num < 0:
            print('p2:',i+1)
            break

if __name__ == '__main__':
    floors = get_input('input.txt')
    print(floors)
    sol(floors)