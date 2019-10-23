def main():
    for _ in range(int(input())):
        n = int(input())
        arr = list(map(int, input().split()))
        mx = max(arr)
        mi = min(arr)
        mx_i = arr.index(mx)
        mi_i = arr.index(mi)
        if mx_i < mi_i:
            print(mx, mi)
        else:
            print(mi, mx)

if __name__ == '__main__':
    main()