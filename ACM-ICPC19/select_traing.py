def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        zero = {}
        one = {}
        for i in range(n):
            s, flag = input().split()
            if flag == '0':
                if s in zero:
                    zero[s] += 1
                else:
                    zero[s] = 1
                if s not in one:
                    one[s] = 0
            else:
                if s in one:
                    one[s] += 1
                else:
                    one[s] = 1
                if s not in zero:
                    zero[s] = 0
        l = list(zero.keys())
        res = 0
        for i in l:
            res += max(zero[i], one[i])
        print(res)

if __name__ == '__main__':
    main()