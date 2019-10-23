def main():
    (n, q) = map(int, input().split())
    d={}
    for _ in range(n-1):
        (a,b) = map(int,input().split())
        if a in d:
            d[a].append(b)
        else:
            d[a] = [b]
        if b in d:
            d[b].append(a)
        else:
            d[b] = []
    for _ in range(q):
        c, D = map(int, input().split())

    print(d)


if __name__ == '__main__':
    main()
