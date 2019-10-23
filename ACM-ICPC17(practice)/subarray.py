def check(arr):
    mul, sum = 1, 0
    for i in arr:
        mul *= i
        sum += i
    if mul == sum:
        #print(arr, 'true')
        return 1
    else:
        #print(arr, 'false')
        return 0

def check1(arr):
    pass


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        count = 0
        for i in range(n):
            for j in range(i, n):
                a = arr[i:j+1]
                count += check(a)
        print(count)

if __name__ == '__main__':
    main()