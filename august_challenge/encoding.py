def f(x):
    x3 = x
    x = list(str(x))
    x1 = [x[0]]
    for i in range(1, len(x)):
        if x[i] == x[i-1]:
            x1.append('0')
        else:
            x1.append(x[i])
    r = int(''.join(x1))
    return r


def main():
    for _ in range(int(input())):
        N_L, L = map(int, input().split())
        N_R, R = map(int, input().split())
        s = 0
        for x in range(L, R+1):
            r = f(x)
            s =(s+ (r))
        print(s)
        '''
        res = R*(R+1)/2 - L*(L-1)/2
        print(res)
        print(res-s, '***********')
        '''


if __name__ == '__main__':
    main()