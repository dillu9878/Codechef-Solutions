def main():
    for _ in range(int(input())):
        (n, m) = map(int, input().split())
        arr = ['1'] * n


        d = {}
        for i in range(m):
            (a, b) = map(int, input().split())
            if a in d:
                d[a] += 1
            else:
                d[a] = 1

            if b in d:
                d[b] += 1
            else:
                d[b] = 1

        if m % 2 == 0:
            print(1)
            print(' '.join(arr))

        else:
            flag = 0
            for i in list(d.keys()):
                if d[i] % 2 != 0:
                    arr[i-1] = '2'
                    flag = 1
                    break
            if flag != 0:
                print(2)
                print(' '.join(arr))
            else:
                print(3)
                arr[a-1] = '2'
                arr[b-1] = '3'
                print(' '.join(arr))


if __name__ =='__main__':
    main()