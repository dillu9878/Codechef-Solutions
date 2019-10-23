def main():
    for _ in range(int(input())):
        n = int(input())
        cp = list(map(int, input().split()))
        h = list(map(int, input().split()))
        s = 0
        for i in range(1, n+1):
            x = max(1, i-cp[i-1])
            y = min(n+1, i+cp[i-1]+1)
            s += y-x
        if s == sum(h):
            print('YES')
        else:
            print('NO')


if __name__ == '__main__':
    main()