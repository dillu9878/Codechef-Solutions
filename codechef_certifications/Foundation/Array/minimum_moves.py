def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        W = list(map(int, input().split()))
        m = max(W)
        s = 0
        for i in W:
            s += m-i
        print(s)


if __name__ == '__main__':
    main()