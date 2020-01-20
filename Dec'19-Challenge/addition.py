def add(A, B):
    count = 0
    while B > 0:
        U = A ^ B
        V = A & B
        A = U
        B = V*2
        print(A, B)
        count += 1
    return count

def main():
    t = int(input())
    for _ in range(t):
        A= int(input(), 2)
        B= int(input(), 2)
        print(add(A, B))


if __name__ == '__main__':
    main()