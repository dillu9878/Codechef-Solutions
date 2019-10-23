def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        s = input()
        r = input()
        s_c = s.count('1')
        r_c = r.count('1')
        if s_c == r_c:
            print('YES')
        else:
            print('NO')


if __name__ == '__main__':
    main()