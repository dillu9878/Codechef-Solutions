def prefix_sum(s):
    Sum = 0
    mod = 10**9+7
    for i in range(1, len(s)-1):
        Sum = (Sum % mod+ int(s[:i])%mod)%mod
    return Sum



def diff_upto_n(n, l, d):
    n1 = str(n)
    s = 0
    mod = 10**9+7
    for i in range(1, l):
        k = ((l - i - 1) * 2)
        if k>20:
            continue
        if k in d:
            p = d.get(k)
        else:
            p = pow(10, k, mod)
            d[k] = p
        if n1[i] > n1[i-1]:
            s = (s % mod + ((int(n1[i - 1]) * (int(n1[i - 1]) + 1)) // 2 * p) % mod) % mod

        elif n1[i] < n1[i-1]:
            s = (s % mod + ((int(n1[i - 1]) * (int(n1[i - 1]) - 1)) // 2 * p) % mod) % mod

        else:
            s = (s % mod + ((int(n1[i - 1]) * (int(n1[i - 1]) - 1)) // 2 * p) % mod) % mod
            v = 0
            if n1[i+1:] != '':
                v = int(n1[i+1:])
            x = l-i-1
            if x in d:
                p1 = d.get(x)
            else:
                p1 = pow(10, (l-i-1), mod)
                d[x] = p1
            s = (s % mod + ((int(n1[i]) % mod) * p1  * ((v+1) % mod)) % mod) % mod

        if n1[:i - 1] != '':
            s = (s % mod + ((int(n1[:i - 1]) % mod) * 45 * p) % mod) %mod
    print(s)
    return s % mod


def sum_upto_n(n):
    mod = 10**9 +7
    #v = pow(2, mod-2,mod)
    v = 500000004
    n = ((n % mod)*((n+1) % mod)) % mod
    return (n * v) % mod


def main():
    t = int(input())
    d= {}
    for _ in range(t):
        nl, l = map(int, input().split())
        nr, r = map(int, input().split())
        l = l-1
        nl = len(str(l))
        d_l = diff_upto_n(l, nl, d)
        d_r = diff_upto_n(r, nr, d)
        s_l = sum_upto_n(l) - d_l
        s_r = sum_upto_n(r) - d_r
        res = s_r - s_l
        print(res%(10**9+7))


if __name__ == '__main__':
    main()
    #print(prefix_sum(str(54438)))