def check(n, A, B):
    count1 = 0
    for i in range(1, A+1):
        for j in range(1, B+1):
            if i*j <= n*n:
                count1 += 1
    count2 = 0
    for i in range(1, n):
        count2 += int((n*n)/i)*2
    print(count2, count1)

def main1():
    t = int(input())
    for _ in range(t):
        (A, B, C) = map(int, input().split())
        count = A * B * C
        for i in range(1, B+1):
            for j in range(1,A+1):
                if j == 1:
                    c = min(C, i*i)
                else:
                    c = min(C, int((i*i)/(j-1)))
                count -= c
                print(i, j, c)
        print(count)
    return count


def main():
    t = int(input())
    for _ in range(t):
        (A, B, C) = map(int, input().split())
        count1 = 0
        for i in range(1,A+1):
            for j in range(1, B+1):
                for k in range(1, C+1):
                    if j*j  <  (i-1)*(k-1):
                        count1 += 1

        count = A * B * C
        for i in range(1, B + 1):
            for j in range(1, A + 1):
                if j == 1:
                    c = min(C, i * i)
                else:
                    c = min(C , int((i * i) / (j - 1)))
                count = count - c -1
                print(i, j, c)
        print(count)
        print(count1)




if __name__ == '__main__':
    main()