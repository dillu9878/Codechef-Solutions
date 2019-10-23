import numpy as np


def main():
    for _ in range(int(input())):
        n = int(input())
        cp = list(map(int, input().split()))
        h = list(map(int, input().split()))
        d = {}
        for i in h:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        a = [0]*n
        for i in range(1, n+1):
            x = max(1, i-cp[i-1])
            y = min(n+1, i+cp[i-1]+1)
            print(x,y)
            x, y = x-1, y-1
            l = np.array(a[x:y])
            a = a[:x] + list(l+ np.ones(len(l))) + a[y:]
            print(a)
            '''
            for j in range(max(1,i- cp[i-1]), min(n+1,i+cp[i-1]+1)):
                if j in range(1, n+1):
                    a[j-1] += 1
            '''
        check = 0
        for i in a:
            if i in d:
                if d[i] == 1:
                    d.pop(i)
                else:
                    d[i] -= 1
            else:
                check = 1
                break

        if check:
            print('NO')
        else:
            print('YES')


if __name__ == '__main__':
    main()
