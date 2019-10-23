def main():
    n = int(input())
    arr = list(map(int, input().split()))
    if n%2==0:
        p = sum(arr[:n//2])
        k = sum(arr[n//2:])
    else:
        p = sum(arr[:n//2+1])
        k = sum(arr[n//2 +1:])
    print(k-p)
    return k-p


if __name__ == '__main__':
    main()