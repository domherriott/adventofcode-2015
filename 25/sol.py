
def sol():
    def pos_to_indx(col, row):
        diag_id = col + row - 1

        counter = 0
        while col > 0:
            counter += 1
            row += 1
            col -= 1

        while diag_id > 0:
            counter += diag_id-1
            diag_id -= 1

        return counter - 1
    
    index = pos_to_indx(3019, 3010)
    codes = [20151125]
    for i in range(1, index+1):
        tmp = (codes[i-1] * 252533)%33554393
        codes.append(int(tmp))
    
    print('solution:', codes[index])

if __name__ == '__main__':
    sol()