# cook your dish here
def main():
    for _ in range(int(input())):
        n = int(input())
        arr = list(map(int, input().split()))
        ans = 0
        for i in range(n):
            count = 0
            if i < 5:
                for j in range(i):
                    if arr[i] < arr[j]:
                        count += 1
                    else:
                        break
                if count == i:
                    ans += 1

            else:
                for j in range(i - 5, i):
                    if arr[i] < arr[j]:
                        count += 1
                    else:
                        break
                if count == 5:
                    ans += 1
        print(ans)


if __name__ == '__main__':
    main()
