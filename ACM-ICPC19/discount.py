def rmv(n, i):
    n = list(n)
    res = n[:i] + n[i+1:]
    res = ''.join(res)
    return int(res)

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        m = []
        l = str(n)
        for i in range(len(l)):
            m.append(rmv(l, i))
        print(min(m))

if __name__ == '__main__':
    main()
