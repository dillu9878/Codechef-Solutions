def main():
    f = open('input2.txt', 'r')
    data = f.readlines()
    f1 = open('output2.txt', 'w')
    for i in data:
        L = i.split(',')
        f1.write('\t'.join(L) + '\n')
    print(data)

if __name__ == '__main__':
    main()