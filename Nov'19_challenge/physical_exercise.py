def point(arr):
    res = []
    for i in range(0, len(arr), 2):
        res.append((arr[i], arr[i+1]))
    return res

def distance(point, arr, p):
    res = []
    for i in arr:
        res.append(((point[0] - i[0]) ** 2 + (point[1] - i[1]) ** 2)  ** (0.5) +  p)
    return res


def tree(root, a, b, c):
    a, b, c = point(a), point(b), point(c)
    d = {root: (a, distance(root, a, 0)), }
    min_distance = 10000000000
    print(d)
    for i in range(len(a)):
        d[a[i]] = (b, distance(a[i], b, d[root][1][i]))
        print(d)
        for j in range(len(b)):
            print(b[j], (c, distance(b[j], c, d[a[i]][1][i])))
            d[b[j]] = (c, distance(b[j], c, d[a[i]][1][i]))
            temp = min(d[b[j]][1])
            if temp < min_distance:
                min_distance = temp
    print(d)
    return min_distance



def main():
    t = int(input())
    for _ in range(t):
        (x, y) = map(int, input().split())
        (n, m, k) = map(int, input().split())
        n_arr = list(map(int, input().split()))
        m_arr = list(map(int, input().split()))
        k_arr = list(map(int, input().split()))
        res = tree((x, y), n_arr, m_arr, k_arr)
        print(res)
        res1 = tree((x,y), m_arr, n_arr, k_arr)
        print(res1)



if __name__ == '__main__':
    main()
