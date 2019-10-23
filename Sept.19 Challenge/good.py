def nck(n, k, mod):
    if k < 0:
        return 0
    sum = 1
    nci = 1
    for i in range(1, k+1):
        nci = (nci * (n - i + 1))%mod
        nci = (nci*pow(i, mod-2, mod)) %mod
        sum = (sum + nci) % mod

    sum %= mod
    return sum

def fin(n, k, mod):
    if k > n//2:
        sum = pow(2, n, mod) - nck(n, n-k-1, mod)
    else:
        sum = nck(n, k, mod)
    return sum


def main():
    mod = 10**9 + 7
    (n, k) = map(int, input().split())
    arr = list(map(int, input().split()))
    d = {}
    arr1 = []
    count = 0
    for i in arr:
        if i in d:
            d[i] += 1
        else:
            arr1.append(i)
            count += 1
            d[i] = 1
    res = 0
    for i in arr1:
        res = (res + d[i] * fin(count-1, k-1, mod))% mod
    print((res*pow(2, mod-2, mod))%mod)


if __name__ == '__main__':
    main()
