def sum_up(arr: list):
    t1, t2 = 0, 0
    for i in range(len(arr)):
        t1 = arr[i] + t2
        arr[i] = str(t1)[-1]
        t2 = t1//10
    return int(''.join(arr[::-1]))

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
    arr = [0]*(3*l)
    for i in range(1, l):
        k = ((l - i - 1) * 2)

        if n1[i] > n1[i-1]:
            arr[k] += ((int(n1[i - 1]) * (int(n1[i - 1]) + 1)) // 2)

        elif n1[i] < n1[i-1]:
            arr[k] += ((int(n1[i - 1]) * (int(n1[i - 1]) - 1)) // 2)
        else:
            arr[k] += ((int(n1[i - 1]) * (int(n1[i - 1]) - 1)) // 2)
            v = 0
            if n1[i+1:] != '':
                v = int(n1[i+1:])
            x = l-i-1

            arr[x] += (int(n1[i]) * (v+1))

        if n1[:i - 1] != '':
            arr[k] += (int(n1[:i - 1]) * 45)
    s = sum_up(arr)
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
    ##print(sum_up([0,0,0,1,450,450]))