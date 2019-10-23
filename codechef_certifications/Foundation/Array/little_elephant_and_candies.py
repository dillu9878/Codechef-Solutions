def main():
    t = int(input())
    for _ in range(t):
        (n, c) = map(int, input().split())
        arr = list(map(int, input().split()))
        s = sum(arr)
        if s > c:
            print('No')
        else:
            print('Yes')


if __name__ == '__main__':
    main()