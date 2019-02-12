import random

def prin(a):
    print()
    print()
    for i in a:
        for j in i:
            print(str(j)+'\t', end='')
        print()

if __name__ == '__main__':
    n = 5
    a = [[random.randint(0,10) for j in range(n)] for i in range(n)]
    rows = []
    cols = []

    prin(a)
    for i in range(n):
        for j in range(n):
            if a[i][j] == 0:
                rows.append(i)
                cols.append(j)
    
    for i in rows:
        for j in range(n):
            a[i][j] = 0

    for i in cols:
        for j in range(n):
            a[j][i] = 0
    
    prin(a)