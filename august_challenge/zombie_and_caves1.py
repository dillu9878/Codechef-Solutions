def add_1(r:list, a:int, b:int):
    for i in range(a, b+1):
        r[i] += 1
    return r


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        C = list(map(int, input().split()))
        H = list(map(int, input().split()))
        H.sort()
        r = [0]*n
        for i in range(n):
            a, b = max(1, C[i]-(i+1)), min(n, C[i]+(i+1))
            a, b = a-1, b-1
            r = add_1(r, a, b)
        r.sort()
        if r == H:
            print('YES')
        else:
            print('NO')


if __name__ =='__main__':
    main()