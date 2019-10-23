def main():
    for _ in range(int(input())):
        (x1, y1, x2, y2) = map(int, input().split())
        if x1 == x2:
            if y2> y1:
                print('up')
            else:
                print('down')
        elif y1 == y2:
            if x2> x1 :
                print('right')
            else:
                print('left')
        else:
            print('sad')

if __name__ == '__main__':
    main()