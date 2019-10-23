def fact(n):
    s = []
    for i in range(1, int(n**0.5)+1):
        if n % i ==0:
            s.append(i)
            if i!=n//i:
                s.append(n//i)
    return s


def diff(s, p):
    print(s, p)
    s = s[::]
    for i in p:
        s.remove(i)
    return len(s)


def main():
    n = int(input())
    arr = list(map(int, input().split()))
    d= {}
    buf = []
    for i in arr:
        f = fact(i)
        d[i] = f
        buf += f
    c = 0
    print(d)
    for i in arr:
        c += diff(buf, d[i])
    print(c)


if __name__=='__main__':
    main()