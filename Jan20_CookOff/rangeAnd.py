def main():
    t = int(input())
    for _ in range(t):
        (l, r) = map(int, input().split())
        # res = l
        # tada1 =l
        # for i in range(l+1, r+1):
        #     res &= i
        #     tada1 += res
        #     print(i, res)
        res1 = 0
        num1 = bin(l)
        num1 = num1[2:]
        num1 = num1[::-1]
        num1 = list(map(int, num1))
        #print(num1)
        dif = r - l
        tada = l
        for j in range(len(num1)):
            if ((2**j)> dif):
                res1 += 2**j
                tada += int(''.join(map(str, num1[::-1])), 2)
            else:
                num1[j] = 0
                tada += int(''.join(map(str, num1[::-1])), 2)
        print(tada)

if __name__ == '__main__':
    main()

