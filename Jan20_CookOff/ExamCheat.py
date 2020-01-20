def fact(a):
    res = []
    for i in range(1, int(a ** (0.5)) + 1):
        if (a % i ==0):
            res.append(i)
            if a//i != i:
                res.append(a//i)

    return res

def main():
    t = int(input())
    for _ in range(t):
        (A, B) = map(int, input().split())
        if A == B :
            print(-1)
        else:
            res = 0
            mx = max(A-1, B-1)
            mi = min(A-1, B-1)
            # if (mx-mi) > mi:
            #     res += 1
            #     print('tada')
            # if mi > 0:
            #     if mx % mi==0:
            #         print('haha')
            #         res+= 1
            # for i in range(1, mi):
            #     if (mx%i == mi % i):
            #         print(i, '----')
            #         res += 1
            # #print(cm(mx, mi), 'yeee')
            res = len(fact(mx-mi))
            print(res)

if __name__ == '__main__':
    main()
    #print(fact(100))
