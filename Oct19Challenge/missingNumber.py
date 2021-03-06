def convert(b, y):
    y = list(y)
    l = len(y)
    for i in range(l):
        if ord(y[i]) > 64:
            y[i] = str(ord(y[i]) - 64 + 9)
    #print(y)
    arr = []
    if b == -1:
        for i in range(max(1, int(max(y))) + 1, 36):
            num = 0
            for j in range(1, l+1):
                num += int(y[j-1]) * pow(i, l-j)

    else:
        num = 0
        for j in range(1, l + 1):
            num += int(y[j - 1]) * pow(b, l - j)

    arr = list(set(arr))
    return arr


def main():
    for _ in range(int(input())):
        n = int(input())
        common = 0
        d = {}
        for i in range(n):
            (b, y) = input().split()
            arr = convert(int(b),y)
            for i in arr:
                if i in d:
                    d[i] += 1
                else:
                    d[i] = 1
        #print(d)
        res = -1
        L = list(d.keys())
        L.sort()
        for i in L:
            if d[i] >= n:
                res = i
                break
        print(res)


if __name__ =='__main__':
    main()