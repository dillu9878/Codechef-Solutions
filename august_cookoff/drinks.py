def main():
    t = int(input())
    for _ in range(t):
        (n,m,k,l,r) = map(int, input().split())
        res = 10**6 +1
        for i in range(n):
            c, p = map(int, input().split())
            if c > k:
                h_t = max(k, c-m)
            else:
                h_t = min(k, c+m)
            if h_t >= l and h_t <=r:
                if res > p:
                    res = p
        if res == (10**6+1):
            print(-1)
        else:
            print(res)


if __name__ == '__main__':
    main()