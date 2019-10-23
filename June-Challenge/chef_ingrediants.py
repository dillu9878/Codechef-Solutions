
def main():
    mod = 10**9 + 7
    t = int(input())
    for i in range(t):
        (n,k) = map(int, input().split())
        a = k-1
        d = (n-1)
        num = int((a+d)/d)

        sn=(num/2)*(2*a - (num-1)*d)
        sn=int(sn)
        print(sn%mod)


if __name__ == '__main__':
    main()

'''
def main():
    mod = 10**9 + 7
    t = int(input())
    for i in range(t):
        (n,k) = map(int, input().split())
        l=list(range(k-1,0,-(n-1)))
        print(sum(l)%mod)


if __name__=='__main__':
    main()
'''