import hashlib

def sol(z):
    key = 'iwrupvqb' 
    i = 0

    while True:
        inp = key + str(i)
        res = hashlib.md5(bytes(inp, encoding='utf-8'))
        res = res.hexdigest()
        if res[:z] == '0'*z:
            print(f'z={z}: {i}')
            return
        i += 1

if __name__ == '__main__':
    sol(z=5)
    sol(z=6)