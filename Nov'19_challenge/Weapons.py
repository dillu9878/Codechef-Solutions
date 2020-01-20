def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        #arr = list(map(int, input().split()))
        res = 0
        for i in range(n):
            inp = int(input(), 2)
            res ^= inp

        print(bin(res).count('1'))

if __name__ == '__main__':
    main()

