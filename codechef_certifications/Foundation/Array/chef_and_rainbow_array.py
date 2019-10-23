def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        d = [0]*10
        check = 1
        for i in range(1, n):
            if (arr[i] == arr[i-1] + 1 or arr[i] == arr[i-1]):
                #
                pass
        if check == -1:
            print('no')
            continue
        if arr == arr[::-1]:
            print('yes')
        else:
            print('no')


if __name__ == '__main__':
    main()