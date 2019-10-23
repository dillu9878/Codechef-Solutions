from itertools import combinations as comb
def common(arr):
    arr.sort()
    #print(arr, 'pair')
    #print(arr[0][1], arr[1][0], arr[2][0])
    if (arr[0][1] >= arr[1][0]) & (arr[0][1] >= arr[2][0]):
        #print('yeah')
        return True
    return False


def check(arr, n):
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                a = [arr[i], arr[j], arr[k]]
                if common(a):
                    return False
    '''
    a = list(comb(arr, 3))
    print(a, 'comb')
    for i in a:
        if common(list(i)):
            return False
    return True
    '''
def main():
    for _ in range(int(input())):
        n = int(input())
        d = {}
        for i in range(n):
            (l, r, v) = map(int, input().split())
            if v in d:
                d[v].append((l, r))
            else:
                d[v] = [(l, r)]

        #print(d, 'v')
        l = list(d.keys())
        flag = True
        for i in l:
            if len(d[i]) > 2:
                flag = check(d[i], len(d[i]))
            if flag == False:
                break
        if flag == False:
            print('NO')
        else:
            print('YES')

if __name__ == '__main__':
    main()