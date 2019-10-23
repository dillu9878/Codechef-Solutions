def main():
    for _ in range(int(input())):
        n = int(input())
        mod = 1000000007
        res = 0
        for i in range(1, n+1):
            res = (res + pow(i, n-i-1, mod))%mod
        print(res)

if __name__ == '__main__':
    main()
