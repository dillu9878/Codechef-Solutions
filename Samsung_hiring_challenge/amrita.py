import pandas as pd

def main():
    data = open('ban-eng.txt', 'r')
    l1 = data.readlines()
    d = {}
    for i in l1[::]:
        l2 = i.split(',')
        for i in l2[1:]:
            if i != '' and i != '\n':
                if i in d:
                    d[i].append(l2[0])
                else:
                    d[i] = [l2[0]]
    eng = open('eng-ban.txt', 'w')
    m = 0
    for i in list(d.keys()):
        eng.write(i)
        li = d[i]
        if len(li) > m:
            m = len(li)
            print(li)
        for j in li:
            eng.write(f',{j}')
        eng.write(','*(5-len(li)))
        eng.write('\n')
    print(m)
    eng.close()

    print(d)

if __name__ == '__main__':
    main()