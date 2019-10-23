def main():
    for _ in range(int(input())):
        s = input()
        s = list(map(int, list(s)))
        if s.count(1) % 2 != 0:
            print('WIN')
        else:
            print('LOSE')


if __name__ =='__main__':
    main()
