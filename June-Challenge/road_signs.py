def main():
    mod=10**9+7
    inp=int(input())
    for j in range(inp):
        k=int(input())
        print((10*pow(2,k-1,mod))%mod)


if __name__=='__main__':
    main()