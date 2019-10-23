def main():
    for _ in range(int(input())):
        n, k = map(int, input().split())
        arr = list(map(int, input().split()))
        arr1 = []
        arr2 = []
        count = 0
        for i in arr:
            if i > k:
                arr1.append(i-k)
                count += 1
            else:
                arr2.append(i)
        if len(arr1)>1:
            arr1.sort()
            a = abs(sum(arr1[:-2]) - arr1[-2])
            print(abs(a - arr1[-1]) + sum(arr2) + k * count)
        else:
            print(sum(arr))



if __name__ =='__main__':
    main()