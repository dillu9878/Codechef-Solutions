def main():
    for _ in range(int(input())):
        n = int(input())
        count = 0
        arr  = [[0 for i in range(n)] for j in range(n)]
        count = 1
        arr[0][0] = 1
        for i in range(n):
            for j in range(i+1):
                arr[j][i-j] = count
                count += 1

        for i in range(1, n):
            c = 0
            for j in range(n-1,i-1,-1):
                arr[i+c][j] = count
                count += 1
                c+=1
        for i in arr:
            print(' '.join(list(map(str,i))))

if __name__ == '__main__':
    main()
