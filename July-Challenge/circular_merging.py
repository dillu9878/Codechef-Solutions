class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.s_left = None
        self.s_right = None


class Circle:
    def __init__(self, arr):
        self.base = Node(arr[0])
        temp = self.base
        l = len(arr)
        for i in range(1, l):
            temp1 = Node(arr[i])
            temp1.right = temp
            temp.left = temp1
            temp = temp1
        self.base.right = temp
        temp.left = self.base

        self.d = {}
        data = self.base.data + self.base.left.data
        self.base2 = Node(data)
        self.d[data] = [self.base2]
        self.base2.s_right = self.base
        self.base2.s_left = self.base.left
        self.base.s_left = self.base2
        self.base.left.s_right = self.base2
        temp2 = self.base2
        temp1 = self.base.left
        for i in range(1, l):
            data = temp1.data + temp1.left.data
            temp3 = Node(data)
            if data not in self.d:
                self.d[data] = [temp3]
            else:
                self.d[data].append(temp3)
            temp3.s_right = temp1
            temp3.s_left = temp1.left
            temp1.s_left = temp3
            temp1.left.s_right = temp3

            temp3.right = temp2
            temp2.left = temp3
            temp2 = temp3
            temp1 = temp1.left
        self.base2.right = temp2
        temp2.left = self.base2

    def merge(self, N):
        N.right.data += N.s_left.data
        N.left.data += N.s_right.data

        N.s_right.data = N.data
        N.s_right.left = N.s_left.left
        N.s_right.s_left = N.s_left.s_left

        N.left.s_right = N.s_right
        N.s_left.left.right = N.s_right

        N.right.left = N.left
        N.left.right = N.right

    def minm(self):
        temp = self.base2
        min, min_o =self.base2.data, self.base2
        l = 0
        while temp.left != self.base2:
            l += 1
            if temp.data <= min:
                min = temp.data
                min_o = temp
            temp = temp.left
        if l<2:
            return -1
        if min_o is self.base2:
            self.base2 = self.base2.left
        return min_o

    def final_merge(self):
        penalty = 0
        while 1:
            N = self.minm()
            if N is -1:
                penalty += self.base2.data
                break
            else:
                penalty += N.data
                self.merge(N)
        return penalty


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        Obj = Circle(arr)
        res = Obj.final_merge()
        print(res)


if __name__ == '__main__':
    main()