def check(arr, i, j, k):
    a, b =0, 0
    for m in range(i, j):
        a = a^arr[m]
    for n in range(j, k+1):
        b = b^arr[n]
    if a == b:
        print(i,j,k)
        return 1
    else:
        return 0



def main():
    for _ in range(int(input())):
        n = int(input())
        arr = list(map(int,input().split()))
        c = 0
        for i in range(n):
            print('************')
            for j in range(i+1, n):
                for k in range(j, n):
                    c += check(arr, i, j,k)
        print(c)


if __name__ == '__main__':
    main()