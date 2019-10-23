def diff_upto_n(n, l):
    n1 = str(n)
    s = 0
    for i in range(1, l):
        s1 = 0
        if n1[i] > n1[i-1]:
            s1 += ((int(n1[i - 1]) * (int(n1[i - 1]) + 1)) // 2 * pow(10, ((l - i - 1) * 2), 10**9+7))

        elif n1[i] < n1[i-1]:
            s1 += ((int(n1[i - 1]) * (int(n1[i - 1]) - 1)) // 2 * pow(10, ((l - i - 1) * 2), 10**9+7))

        else:
            s1 += ((int(n1[i - 1]) * (int(n1[i - 1]) - 1)) // 2 * pow(10, ((l - i - 1) * 2), 10**9+7))
            v = 0
            if n1[i+1:] != '':
                v = int(n1[i+1:])
            s1 += int(n1[i]) * pow(10, (l-i-1),10**9+7) * (v+1)

        if n1[:i - 1] != '':
            s1 += (int(n1[:i - 1]) * 45 * pow(10, ((l - i - 1) * 2), 10**9+7))
        s = (s + s1) % 10**9+7
    return s


def sum_upto_n(n):
    return (n*(n+1)//2)%(10**9+7)


def main():
    t = int(input())
    for _ in range(t):
        nl, l = map(int, input().split())
        nr, r = map(int, input().split())
        l = l-1
        nl = len(str(l))
        d_l = diff_upto_n(l, nl)
        d_r = diff_upto_n(r, nr)
        s_l = sum_upto_n(l) - d_l
        s_r = sum_upto_n(r) - d_r
        res = s_r - s_l
        print(res)


if __name__ == '__main__':
    main()