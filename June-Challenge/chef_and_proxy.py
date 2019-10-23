def main():
    for _ in range(int(input())):
        day=int(input())
        r_p=day*0.75
        if r_p > int(r_p):
            r_p=int(r_p)+1

        s=input()
        p=s.count('P')
        c=0

        for i in range(2, day-2):
            if p >= r_p:
                break
            if s[i] == 'A':
                if (s[i-1] == 'P' or s[i-2] == 'P') and (s[i+1]=='P' or s[i+2]=='P'):
                    p += 1
                    c += 1
        if p >= r_p:
            print(c)
        else:
            print(-1)


if __name__ == '__main__':
    main()