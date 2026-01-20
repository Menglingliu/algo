class QuickFind:
    def __init__(self, N):
        self.id = list(range(N))

    def connect(self, p, q):
        p_id = self.id[p]
        q_id = self.id[q]
        for i in range(len(self.id)):
            if self.id[i] == p_id:
                self.id[i] = q_id

    def is_connected(self, p, q):
        return self.id[p] == self.id[q]


test = QuickFind(5)
test.connect(1, 2)
test.connect(1, 3)
test.connect(4, 0)
test.connect(0, 2)
print(test.is_connected(1,0))
print(test.is_connected(4,3))


# Time complexity: o(n)
# Space complexity: o(n)