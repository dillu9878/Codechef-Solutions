def main():
    (n,k) = map(int, input().split())
    arr = list(map(int,  input().split()))
    Max, s = 0, 0
    arr1 = [0]
    for i in range(n):
        s += arr[i]
        arr1.append(s)
    for i in range(k,n+1):
        s = arr1[i] - arr1[i-k]
        if s > Max:
            Max = s
    print(Max)


if __name__ == '__main__':
    main()