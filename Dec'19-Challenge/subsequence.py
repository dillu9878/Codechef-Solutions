def check(s):
    pass


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        s= input()
        global d
        d = {}
        i = 0
        for c in s:
            if c in d:
                d[c].append(i)
            else:
                d[c] = [i]
            i += 1
        for i in range(n//2, 0, -1):
            for j in range(0, n):
                temp  = s[j: j+i]
                if len(temp) >= i:
                    print(temp)


if __name__ == '__main__':
    main()
