def main():
    t = int(input())
    for _ in range(t):
        (n, m, q) = map(int, input().split())
        dx, dy = {}, {}
        for i in range(q):
            (x, y) = map(int, input().split())
            if x in dx:
                dx[x] += 1
            else:
                dx[x] = 1
            if y in dy:
                dy[y] += 1
            else:
                dy[y] = 1
        e_x, o_x, e_y, o_y = 0, 0, 0, 0
        lx, ly = list(dx.keys()), list(dy.keys())
        for i in lx:
            if dx[i] % 2 == 0:
                e_x += 1
            else:
                o_x += 1
        for i in ly:
            if dy[i] % 2 == 0:
                e_y += 1
            else:
                o_y += 1
        #res = e_x*(n - e_y) + o_x*(n - o_y)
        #res = res + (o_x *(n - len(lx))) + (o_y*(n - len(ly)))
        res = o_x*(m - o_y) + (n - o_x) * o_y
        print(res)

if __name__ == '__main__':
    main()