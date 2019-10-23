def main():
    t = int(input())
    for _ in range(t):
        (n, m) = map(int, input().split())
        if m < n-1  or m > ((n+1)*n)/2:
            print(-1)
        elif m <= n+1:
            print(2)
        elif m <= 2*n:
            print(3)
        else:
            k = m - 2*n
            i = 1
            s = 0
            while 1:
                if i % 2 == 0:
                    s += (n//2 + 1)
                else:
                    s += n//2
                if s >= k:
                    print(3 + i)
                    break
                i += 1



if __name__ == '__main__':
    main()