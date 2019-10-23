def diff_p(l):
    s = 0
    n = len(l)
    for i in range(n - 1, -1, -1):
        s += i * l[i] - (n - 1 - i) * l[i]
    s -= n*(n-1)//2
    return s


def main():
    for _ in range(int(input())):
        n = int(input())
        arr = list(map(int, input().split()))
        s = 0
        v = 0
        d = {0:[-1]}
        s = 0
        a = []
        for i in range(0, n):
            v = v ^ arr[i]
            if v in d:
                d[v].append(i)
            else:
                d[v] = [i]
        for i in list(d.keys()):
            s += diff_p(d.get(i))
        print(s)


if __name__ == '__main__':
    main()