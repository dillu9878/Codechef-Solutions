from bisect import bisect_left

def count1(l):
    n = len(l)
    a=l[:]
    b=[]
    a.sort()
    for i in range(n):
        k=l[i]
        x=bisect_left(a,k)
        b.append((x))
        del a[x]
    return sum(b)



def main():
    for _ in  range(int(input())):
        (n, k) = map(int, input().split())
        arr = list(map(int, input().split()))
        x = len(list(set(arr[::])))
        n =x 
        res = k * count1(arr)
        res  += ((n*(n-1)) * (k*(k-1)))/4
        print(int(res))
        

if __name__ == '__main__':
    #print(count1([1, 2 , 1]))
    main()

