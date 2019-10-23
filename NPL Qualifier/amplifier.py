def main():
    for _ in range(int(input())):
        n = int(input())
        x = int(input())
        d = {}
        a, b = [], []
        for i in range(n):
            (ai, bi) = map(int, input().split())
            if ai in d:
                d[ai].append(bi)
                d[ai] = d[ai].sort()[::-1]
            else:
                d[ai] = [bi]

        l = list(d.keys())
        l.sort()
        l1 = d[l[0]]
        d[l[0]] = l1[:-1]
        x = l[0] * x + l1[-1]
        l = l[::-1]
        for i in l:
            l2 = d[i]
            for j in l2:
                x = x*i + j
        print(x)


if __name__ == '__main__':
    main()
