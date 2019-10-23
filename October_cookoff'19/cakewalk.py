import math

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())

        x, y = 0, 0
        #x1 = math.log(n, 10)
        while n % 10 == 0 and n > 0:
            x += 1
            n = n // 10

        y = math.log2(n)

        #print(x1, y)
        if x >= y and y == int(y):
            print('Yes')
        else:
            print('No')


if __name__ == '__main__':
    main()