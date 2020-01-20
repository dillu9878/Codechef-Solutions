def main():
    for _  in range(int(input())):
        n  = int(input())
        arr  = list(map(int, input().split()))
        arr.sort()
        x = arr[n//4]
        if arr[(n//4) - 1] == x:
            print(-1)
            continue
        y = arr[n//2]
        if arr[n//2 - 1] == y:
            print(-1)
            continue
        
        z = arr[3*(n//4)]
        if arr[3*(n//4) - 1] == z:
            print(-1)
            continue
            
        print(x, y, z)

if __name__ == '__main__':
    main()