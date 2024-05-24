class UnionFind:
    def __init__(self):
        self.father = {}
        self.count = 0

    def add(self, x):
        if x not in self.father:
            self.father[x] = None
        self.count += 1

    def find(self, x):
        root = x
        while self.father[x] is not None: root = self.father[x]
        while x != root:
            original_root = self.father[x]
            self.father[x] = root
            x = original_root
        return root

    def merge(self,x,y):
        px, py = self.find(x), self.find(y)
        if px != py:
            self.father[x] = py
        self.count -= 1


class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        uf = UnionFind()
        # traverse the matrix
        for i in range(len(M)):
            uf.add(i)
            # Given the representative matrix is symmetric and the diagonal is 1
            # we only traverse the upper-left triangle
            for j in range(i):
                if M[i][j]:
                    uf.merge(i, j)
        return uf.count

