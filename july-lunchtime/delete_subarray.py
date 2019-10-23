def sum_digit(n):
    return sum(list(map(int,list(str(n)))))
def main():
    for _ in range(int(input())):
        n = int(input())
        arr = list(map(int, input().split()))
        arr1 = []
        Max = 0
        for i in range(n):
            for j in range(i+1, n):
                arr1.append(sum_digit(arr[i]* arr[j]))
        print(max(arr1))


if __name__ == '__main__':
    main()

