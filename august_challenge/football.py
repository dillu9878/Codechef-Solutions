def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        A = list(map(int, input().split()))
        B = list(map(int, input().split()))
        Max = 0
        for i in range(n):
            s = A[i]*20 - B[i]*10
            if Max < s:
                Max = s
        print(Max)


if __name__ == '__main__':
    main()