def count(s):
    E, O = 0, 0
    for i in s:
        if bin(i).count('1') % 2 == 0:
            E += 1
        else:
            O += 1
    return E, O


def parityOf(int_type):
    parity = 0
    while (int_type):
        parity = ~parity
        int_type = int_type & (int_type - 1)
    return(parity)


def parity_again():
    t = int(input())
    for _ in range(t):
        q = int(input())
        s = set([])
        for i in range(q):
            x = int(input())
            for j in list(s):
                s.add(j ^ x)
            s.add(x)
            print(s)
            E, O = count(s)
            print(E, O)


if __name__ == '__main__':
    print(parityOf(1))
            

