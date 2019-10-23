def main():
    t = int(input())
    for _ in range(t):
        [n, s] = list(input().split())
        n = int(n)
        one, zero = 0, 0
        for i in range(n):
            s1 = input()
            if s1[0] == '0':
                zero += s1.count('0')
            else:
                one += s1.count('1')
        if zero > one:
            print('Dee')
        elif zero < one:
            print('Dum')
        else:
            if s == 'Dee':
                print('Dum')
            else:
                print('Dee')

if __name__ == "__main__":
    main()

