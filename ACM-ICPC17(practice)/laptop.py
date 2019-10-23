def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        d = {}
        for i in arr:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        l = list(d.keys())
        #print(d)
        m = max(l)
        for i in l:
            if d[i] == 1 and i < m:
                m = i
        print(m)

if __name__ == '__main__':
    main()