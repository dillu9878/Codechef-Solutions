def factor(n, d):
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
            if i != n//i:
                if n//i in d:
                    d[n//i] += 1
                else:
                    d[n//i] = 1
    return d

def main():
    for _ in range(int(input())):
        n = int(input())
        arr = list(map(int, input().split()))
        d = {}
        Max = 0
        for i in arr:
            if i in d:
                if d[i] > Max:
                    Max = d[i]
            d = factor(i, d)
        print(Max)


if __name__ == '__main__':
    #print(factor(28))
    main()