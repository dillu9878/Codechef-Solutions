def max_diff(arr1, arr2):
    diff = 0
    for i in range(26):
        temp = arr2[i]-arr1[i]
        if temp>diff:
            diff = temp
    return diff


def main():
    t = int(input())
    for _ in range(t):
        (n, q) = map(int, input().split())
        s = input()
        a = [0]*26
        a[97 - ord(s[0])] = 1
        d = {0:a[::]}
        for i in range(1, n):
            a = d[i-1][::]
            a[97-ord(s[i])] += 1
            print(a)
            d[i] = a
        print(d)
        for i in range(q):
            (l,r) = map(int, input().split())
            diff = max_diff(d[l-1], d[r-1])
            li = r-l+1
            print(li,diff)
            if diff>= li//2:
                print('YES')
            else:
                print('NO')



if __name__ == '__main__':
    main()