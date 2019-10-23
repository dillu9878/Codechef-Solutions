def main():
    for _ in range(int(input())):
        (n, k) = map(int, input().split())
        arr = list(map(int, input().split()))
        arr1 = arr[::]
        if (k//n) % 3 == 1:
            for i in range(n//2):
                arr[n-i-1], arr[i]=arr[i], arr[i] ^ arr[n-i-1]
            if n%2 !=0:
                arr[n//2] = 0
        elif (k//n) % 3 == 2:
            for i in range(n//2):
                arr[i], arr[n-i-1] = arr[n-i-1], arr[i] ^ arr[n-i-1]
            if n%2 !=0:
                arr[n//2] = 0
        else:
            if n%2 !=0 and k > n//2:
                arr[n//2] = 0

        for i in range(k%n):
            arr[i] = arr[i] ^ arr[n-i-1]
        print(' '.join(map(str, arr)))
'''
        for i in range(k):
            arr1[(i%n)] = arr1[i%n] ^ arr1[(n-(i%n)-1)]
        print(' '.join(map(str, arr1)))
'''

if __name__ == '__main__':
    main()
