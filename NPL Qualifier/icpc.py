from collections import Counter




def main():
    n = int(input())
    arr = []
    d = []
    count = 0
    for i in range(n):
        s = input()
        s1 = Counter(s)
        if s1 not in d:
            d.append(s1)
            count += 1
        arr.append(count)
    print(d)
    print(arr)
    q = int(input())
    #arr = [1, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7]
    for i in range(q):
        (l, r) = map(int, input().split())
        if l == 1:
            v = 0
        else:
            v = arr[l-2]
        res = arr[r - 1] - v
        print(res)


if __name__ == '__main__':
    main()