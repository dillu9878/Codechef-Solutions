def main():
    t = int(input())
    for _ in range(t):
        l = int(input())
        if l == 1:
            print(0)
        elif l <= 3:
            print(1)
        else:
            d = {3: 2, 0: 3, 1: 0, 2: 9}
            p = len(bin(l)) - 2
            p = p % 4
            print(d[p])


if __name__ == '__main__':
    main()
