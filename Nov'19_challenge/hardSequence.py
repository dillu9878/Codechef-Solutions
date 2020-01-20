def series(n):
    arr = [0, 0, 1, 0, 2, 0, 2, 2, 1]
    d = {0:[1,2, 4, 6], 1:[3, 9], 2:[5, 7, 8]}
    for i in range(9, n):
        if len(d[arr[-1]]) == 1:
            arr.append(0)
            d[0].append(i+1)
        else:
            v = d[arr[-1]]
            next_element = v[-1] - v[-2]
            arr.append(next_element)
            if next_element in d:
                d[next_element].append(i+1)
            else:
                d[next_element] = [i+1]
    return arr

def positionCounter(arr):
    res, count = [], {}
    for i in arr:
        if i in count:
            v = count[i] + 1
            count[i] = v
        else:
            v = 1
            count[i] = 1
        res.append(v)
    return res



def main():
    arr = series(128)
    #print(arr)
    res = positionCounter(arr)
    #print(res)
    for _ in range(int(input())):
        n = int(input())
        print(res[n-1])

if __name__ == '__main__':
    main()