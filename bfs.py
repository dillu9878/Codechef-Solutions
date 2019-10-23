class Node:
    def __init__(self, v):
        self.vertex = v
        self.next = None


class Graph:
    def __init__(self, v, e):
        self.visited = {}
        self.temp = []

        self.g = {}
        for i in range(v):
            self.g[i] = []

        for edge in range(e):
            (a, b) = map(int, input('Enter edge(a->b)').split())
            if a in self.g:
                self.g[a].append(b)
            else:
                self.g[a] = [a]

            if b in self.g:
                self.g[b].append(a)
            else:
                self.g[b] = [a]

    def bfs(self, startNode):
        currentNode = startNode
        if currentNode not in self.visited:
            self.temp = self.temp[1:] + self.g[currentNode]

            print(str(currentNode) + '->>>', end = '')
            self.visited[currentNode] = True
        else:
            self.temp = self.temp[1:]

        if self.temp == []:
            return 'Done'
        else:
            currentNode = self.temp[0]
            return self.bfs(currentNode)


def main():
    (v, e) = map(int, input('Enter number of vertex and edge: ').split())
    G1 = Graph(v, e)
    start = int(input('Enter start node: '))
    G1.bfs(start)


if __name__ == '__main__':
    main()