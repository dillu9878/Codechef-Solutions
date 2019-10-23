def main():
    t = int(input())
    for _ in range(t):
        (A, B, C) = map(int, input().split())
        count = A * C *B
        for k in range(1, B+1):
            for i in range(1, A+1):
                count -= min(C, int(k*k/i))
        count1 = A*C*B
        for i in range(1, A+1):
            for j in range(1, C+1):
                for k in range(1, B+1):
                    if i*j <= k*k:
                        count1 -= 1
        print(count, count1)

if __name__ == '__main__':
    main()