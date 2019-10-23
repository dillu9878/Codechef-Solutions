class Node:
    def __init__(self, data, parent = None):
        self.data = data
        self.child = []
        self.parent = parent


class Tree:
    def __init__(self):
        self.root = None
        self.d = {}
    def start(self, u, v):
        a = Node(u)
        b = Node(v, a)
        self.root = a
        self.root.child.append(b)
        self.d[u] = a
        self.d[v] = b

    def add_node(self, u, v):
        if u in self.d:
            a = Node(v, self.d[u])
            self.d[u].child.append(a)
            self.d[v] = a
        elif v in self.d:
            a = Node(u, self.d[v])
            self.d[v].child.append(a)
            self.d[u] = a
        else:
            pass
    def find_triplets(self):
        pass



def main():
    for _ in range(int(input())):
        n = int(input())
        p1, p2, p3 = map(int, input().split())
        d = {}
        t_d = {}
        (v, c) = map(int, input().split())
        T = Tree()
        T.start(v, c)
        for i in range(1, n-1):
            (v, c) = map(int, input().split())
            T.add_node(v, c)
        print(T.d)


if __name__ == '__main__':
    main()