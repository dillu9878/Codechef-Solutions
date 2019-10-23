def main():
    mod = 10**9 + 7
    for _ in range(int(input())):
        n = int(input())
        if  n == 0:
            print(0, 0)
            continue
        e = pow(2, n-1, mod)

        print(e -1, e)

if __name__=='__main__':
    main()
