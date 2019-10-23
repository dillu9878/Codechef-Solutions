def diff_upto_n(n, l):
    mod = 10**9+7
    n1 = str(n)
    s = 0
    for i in range(1, l):
        if n1[i] > n1[i-1]:
            s = (s%mod + ((int(n1[i - 1]) * (int(n1[i - 1]) + 1)) // 2 * pow(10, ((l - i - 1) * 2), mod))%mod)%(mod)

        elif n1[i] < n1[i-1]:
            s = (s%mod + ((int(n1[i - 1]) * (int(n1[i - 1]) - 1)) // 2 * pow(10, ((l - i - 1) * 2), mod))%mod)%(mod)

        else:
            s = (s%mod + ((int(n1[i - 1]) * (int(n1[i - 1]) - 1)) // 2 * pow(10, ((l - i - 1) * 2), mod))%mod)%(mod)
            v = 0
            if n1[i+1:] != '':
                v = int(n1[i+1:])
            s = (s%mod + ((int(n1[i])%mod) * pow(10, (l-i-1), (mod)) * ((v+1)%mod))%mod)%(mod)

        if n1[:i - 1] != '':
            s = (s%mod + ((int(n1[:i - 1])%(mod)) * 45 * pow(10, ((l - i - 1) * 2), mod)%mod)%mod)%(mod)

    return s%mod


def sum_upto_n(n):
    mod = 10**9+7
    return (((n%mod)*((n+1)%mod))%mod)//2


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
        print(res%(10**9+7))


if __name__ == '__main__':
    main()