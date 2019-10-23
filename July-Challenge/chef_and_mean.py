def chef_and_coins():
    t = int(input())
    for _  in range(t):
        n = int(input())
        arr = list(map(int,input().split()))
        s = sum(arr)
        mean = s/n
        if mean in arr:
            print(arr.index(mean) + 1)
        else:
            print('Impossible')


if __name__== '__main__':
    chef_and_coins()