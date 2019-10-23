def main():
    for _ in range(int(input())):
        n = int(input())
        d = {}
        arr = list(map(int, input().split()))
        flag = 0
        for i in arr:
            if ((i > 1) or (i < -1)) and i in d:
                print('no')
                flag = 1
                break
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        if flag:
            continue
        l = list(d.keys())
        if len(l) == 1:
            if n == 1:
                print('yes')
            else:
                if (1 in l) or (0 in l):
                    print('yes')
                else:
                    print('no')
        elif len(l) == 2:
            if (0 in l):
                if -1 in d:
                    if d[-1] == 1:
                        print('yes')
                    else:
                        print('no')
                else:
                    print('yes')
            elif 1 in l:
                print('yes')
            else:
                print('no')
        elif len(l) == 3:
            if (0 in l) and (1 in l):
                print('yes')
            else:
                print('no')
        else:
            print('no')


if __name__== '__main__':
    main()
