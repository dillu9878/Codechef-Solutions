def main():
    t = int(input())
    for k in range(1, t+1):
        l = k
        arr = []
        for i in range(l):
            if i == 0:
                arr.append(0)
            elif i == 1:
                arr.append(1)
            else:
                arr.append(arr[-2] + arr[-1])
        while len(arr) >= 2:
            arr = arr[1::2]

        res = str(arr[0])[-1]

        l = k
        if l == 1:
            ans = '0'
        elif l <= 3:
            ans = '1'
        else:
            d = {3: '2', 0: '3', 1: '0', 2: '9'}
            p = len(bin(l)) - 2
            p = p % 4
            ans = d[p]
        if res != ans:
            print(l, '-->', res, ans)

if __name__ == '__main__':
    main()