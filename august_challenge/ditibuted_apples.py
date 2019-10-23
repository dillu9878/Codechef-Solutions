def main():
    t = int(input())
    for _ in range(t):
        (n, k) = map(int, input().split())
        if n%(k*k)==0:
            print('NO')
        else:
            print('YES')


if __name__ == '__main__':
    main()