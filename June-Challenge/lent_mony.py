def main():
    t = int(input())
    for _ in range(t):
        '''
        n = int(input())
        arr = list(map(int, input().split()))
        k = int(input())
        '''
        x = int(input())
        l=[]
        for i in range(100):
            l.append(i^x)
        print(l)
        print(sum(l), sum(list(range(100))))


if __name__ == '__main__':
    main()
