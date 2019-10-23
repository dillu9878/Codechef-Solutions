# cook your dish here
def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        left = []
        right = []
        s_left, s_right = 0, 0
        for i in range(n):
            s = input()
            s1, s2 = s[:n//2+1], s[n//2+1:]
            x, y = s1.count('1'), s2.count('1')
            s_left += x
            s_right += y
            left.append(x)
            right.append(y)
        diff = s_left - s_right
        min_diff = abs(diff)

        for i in range(n):
            if min_diff == 0:
                break
            temp = abs(diff - 2*(left[i] - right[i]))
            if temp < min_diff:
                min_diff = temp
        print(min_diff)


if __name__ == '__main__':
    main()