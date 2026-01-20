class QuickUnion:
    def __init__(self, N):
        self.parent = [-1] * N

    def find(self, p):
        r = p
        while self.parent[r] >= 0:
            r = self.parent[r]
        return r

    def is_connected(self, p, q):
        return self.find(p) == self.find(q)

    def connect(self, p, q):
        i = self.find(p)
        j = self.find(q)
        self.parent[i] = j

