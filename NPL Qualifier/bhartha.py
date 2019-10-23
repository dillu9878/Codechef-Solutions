def main():
    for _ in range(int( input())):
        s = input()
        l, d = [], {}
        for i in s:
            if i not in d:
                d[i] = 1
                l.append(i)
        print(''.join(l))

if __name__ == '__main__':
    main()