def main():
    f = open('input.txt', 'r')
    l = f.readlines()
    f1 = open('output.txt', 'w')
    for i in l:
        arr = i.split('\t')
        arr[-1] = arr[-1][:-1]
        f1.write(','.join(arr))
        f1.write('\n')
    f.close()
    f1.close()

if __name__ == '__main__':
    main()
