def main():
    for _ in range(int(input())):
        (n, k, p) = map(int, input().split())
        arr = list(map(int, input().split()))

        if k%2 == 0:
            if p == 0:
                mx = 0
                if n == 2:
                    mx = max(arr)
                    print(mx)
                    continue

                for i in range(1, n-1):
                    temp = min(arr[i-1], arr[i+1])
                    if temp > mx:
                        mx = temp
                
                if arr[1] > mx:
                    mx = arr[1]
                if arr[-2] > mx:
                    mx = arr[-2]

                print(mx)
            else:
                mn = max(arr)
                if n == 2:
                    mn = min(arr)
                    print(mn)
                    continue
                

                for i in range(1, n-1):
                    temp = max(arr[i-1], arr[i+1])
                    if temp < mn:
                        mn = temp
                if arr[1] < mn:
                    mn = arr[1]
                if arr[-2] < mn:
                    mn =arr[-2]
                print(mn)

        else:
            if p == 0:
                print(max(arr))
            else:
                print(min(arr))


if __name__ == '__main__':
    main()
