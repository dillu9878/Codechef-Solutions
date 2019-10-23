def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        d = {}
        for i in arr:
            if i in d:
                d[i] += 1
            else:
                d[i]= 1
        count=0
        print(n - d[arr[0]] - count, end=' ')
        for i in range(1, n):
            if arr[i] !=arr[i-1]:
                count +=1
            print(n-d[arr[i]]-count, end=' ')

        print()

if __name__ == '__main__':
    main()