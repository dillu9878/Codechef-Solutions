def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        left = []
        right = []
        s_left, s_right = 0, 0
        Min, Max = 1000, -1000
        for i in range(n):
            s = input()
            s1, s2 = s[:n//2], s[n//2:]
            x, y = s1.count('1'), s2.count('1')
            s_left += x
            s_right += y
            d = x-y
            if d > Max:
                Max = d
            if d < Min:
                Min = d

            left.append(x)
            right.append(y)
        diff = s_left - s_right
        '''
        print(diff)
        if diff >0:
            min_diff = abs(diff- 2*Max)
        elif diff < 0:
            min_diff = abs(diff - 2*Min)
        else:
            min_diff = 0


        '''
        min_diff1 = abs(diff)

        for i in range(n):
            if min_diff1 == 0:
                break
            temp = abs(diff - 2*(left[i] - right[i]))
            if temp < min_diff1:
                min_diff1 = temp
        print(min_diff1)


if __name__ == '__main__':
    main()

