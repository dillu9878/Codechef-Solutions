import numpy as np


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        C = list(map(int, input().split()))
        H = list(map(int, input().split()))
        H.sort()
        h = np.array(H)
        r = np.zeros(n)
        for i in range(n):
            a, b = max(1, C[i]-(i+1)), min(n, C[i]+(i+1))
            a, b = a-1, b-1
            l = len(r[a:b])
            r = np.concatenate([r[:a], r[a:b]+np.ones(l), r[b:]])
        r.sort()
        r = h[r!=h]
        if len(r)>0:
            print('NO')
        else:
            print('YES')


if __name__ =='__main__':
    main()
