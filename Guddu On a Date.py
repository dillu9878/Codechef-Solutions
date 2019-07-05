def sum_of_digit(n):
    s=0
    for i in str(n):
        s+=int(i)
    return s

def main():
    List=[19]
    list2=[]
    t=int(input())
    for k in range(1,t):
       n=k
       i=len(List)
       start=List[-1]+1
       while i<n:
           if sum_of_digit(start)%10==0:
               List.append(start)
               i += 1
           start += 1
       list2.append(n*10+(10-sum_of_digit(n*10))%10)
    print(List)
    print(list2)
    print(List==list2)


if __name__=='__main__':
    main()
