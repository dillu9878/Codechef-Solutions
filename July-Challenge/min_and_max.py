def min_and_max():
    t = int(input())
    for _ in range(t):
        n = int(input())
        k = int(input())
        mod = k%n
        m = min(mod, n - mod)
        Max = 2*m
        if m is n/2:
            Max = Max-1
        print(Max)


if __name__ == '__main__':
    min_and_max()