def main():
    t = int(input())
    for _ in range(t):
        (x, y, k, n) = map(int, input().split())
        z = x - y
        check = 0
        for i in range(n):
            pi, ci = map(int, input().split())
            if pi >= z and k >= ci:
                check = 1
                break
        if check:
            print('LuckyChef')
        else:
            print('UnluckyChef')


if __name__ == '__main__':
    main()