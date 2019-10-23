def main():
    t = int(input())
    for _ in range(t):
        (l, r) = map(int, input().split())
        l1, r1 = bin(l), bin(r)
        l1, r1 = l1[2:], r1[2:]
        l2, r2 = len(l1), len(r1)
        if l2 < r2:
            print(2 **(r2) - 1)
        else:
            count = 0
            for i in range(r2):
                if l1[i] != r1[i]:
                    break
                count += 1
            s = r1[: count] + '1'*(r2 - count)
            #print(s)
            print(int(s, 2))

if __name__ == '__main__':
    main()