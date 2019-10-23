def main():
    p = {(1,2,3): '<>', (3,2,1): '><', (1,3,2): '<<<', (2,3,1): '<<>', (2,1,3): '>><',  (3,1,2): '>>>'}
    for _ in range(int(input())):
        n = int(input())
        p1, p2, p3 = map(int, input().split())
        d = {}
        for i in range(n-1):
            (v, c) = map(int, input().split())
            if v in d:
                if c < v:
                    d[v][0].append(c)
                else:
                    d[v][1].append(c)
            else:
                if c < v:
                    d[v] = [[c], []]
                else:
                    d[v] = [[], [c]]
            if c in d:
                if c > v:
                    d[c][0].append(v)
                else:
                    d[c][1].append(v)
            else:
                if c > v:
                    d[c] = [[v], []]
                else:
                    d[c] = [[], [v]]
        s = 0
        t = p.get((p1,p2,p3))
        for i in list(d.keys()):
            if t == '<>' or t == '><':
                s += len(d[i][0]) * len(d[i][1])
            elif t == '>><' or t == '>>>':
                l = len(d[i][1])
                s += (l*(l-1))//2
            else:
                l = len(d[i][0])
                s += (l*(l-1))//2


        l = list(d.keys())
        l.sort()
        s1 = 0
        for i in range(len(l)):

            if t == '<>' or t == '><':
                s1 += i*(n-i-1)
            elif t == '>><' or t == '>>>':
                s1 += (i*(i-1))//2
            else:
                k = n-i-1
                s1 += (k*(k-1))//2

        print(s1)


if __name__ == '__main__':
    main()