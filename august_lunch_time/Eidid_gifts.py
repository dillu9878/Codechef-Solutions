def main():
    t = int(input())
    for _ in range(t):
        (a1, a2, a3, c1, c2, c3) = map(int, input().split())
        da = {a1: '1', a2: '2', a3:  '3'}
        dc = {c1: '1', c2: '2', c3:  '3'}
        a = [a1, a2, a3]
        c = [c1, c2, c3]
        a.sort()
        c.sort()
        maxage = da[a[-1]]
        minage = da[a[0]]
        midage = da[a[1]]

        maxc = dc[c[-1]]
        minc = dc[c[0]]
        midc = dc[c[1]]
