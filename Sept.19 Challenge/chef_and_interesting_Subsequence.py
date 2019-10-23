# cook your dish here
def fact(n):
    f = 1
    for i in range(2, n+1):
        f *= i

    return f


def main():
    t = int(input())
    for _ in range(t):
        (n, k) = map(int,  input().split())
        arr = list(map(int, input().split()))
        arr.sort()
        temp = arr[k-1]
        count1 = 0
        i = k
        while 1:
            if i < n:
                if arr[i] == temp:
                    count1 += 1
                    i+=1
                else:
                    break
            else:
                break
        i = k-1
        count2 = 0
        while 1:
            if i > -1:
                if arr[i] == temp:
                    count2 += 1
                    i -= 1
                else:
                    break
            else:
                break

        res = fact(count1 + count2)/(fact(count1) * fact(count2))
        print(int(res))


if __name__ == '__main__':
    main()
