def Sum(arr):
    res = 0
    for i in range(1,len(arr)+1):
        res += i*arr[i-1]
    return res


def Max(arr):
    ind = -1
    p = 0
    for i in range(1, len(arr)):
        c = (i+1) * arr[i] + i*arr[i-1]
        s = i*arr[i] + (i+1) * arr[i-1]
        if s > c and s > p:
            ind = i
            p = s
    return ind


def swap(arr):
    if len(arr) <= 1:
        return arr
    i = Max(arr)
    if i == -1:
        return arr
    return swap(arr[:i-1]) +[arr[i], arr[i-1]] + swap(arr[i+1:])


def main():
    for _ in range(int(input())):
        n = int(input())
        arr = list(map(int,  input().split()))
        swapped_arr = swap(arr)
        print(swapped_arr)
        print(Sum(swapped_arr))


if __name__ == '__main__':
    main()