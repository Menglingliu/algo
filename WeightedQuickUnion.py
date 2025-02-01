class WeightedQuickUnion:
    def __init__(self, N):
        self.parent = list(range(N))
    
    def find(self, r):
        if self.parent[r] != r:
            # return self.find(self.parent[r]) # if not to connect
            self.parent[r] = self.find(self.parent[r]) # path compression
        # print(r, self.parent[r])
        return self.parent[r]
    
    def connect(self, p, q):
        i = self.find(p)
        j = self.find(q)
        if i == j:
            return
        self.parent[i] = j
    
    def is_connected(self, p, q):
        return self.find(p) == self.find(q)


test = WeightedQuickUnion(5)
test.connect(1, 2)
test.connect(1, 3)
test.connect(4, 0)
test.connect(0, 2)
print(test.find(4))
print(test.find(1))
print(test.find(2))
print(test.find(3))
print(test.is_connected(1,0))

# class WeightedQuickUnion:
#     def __init__(self, N):
#         self.parent = [i for i in range(N)]
#         self.size = [1] * N
    
#     def find(self, r):
#         if self.parent[r] != r:
#             # return self.find(self.parent[r]) # if not to connect
#             self.parent[r] = self.find(self.parent[r])
#         # print(r, self.parent[r])
#         return self.parent[r]
    
#     def connect(self, p, q):
#         i = self.find(p)
#         j = self.find(q)
#         if i == j:
#             return
#         if self.size[i] < self.size[j]:
#             self.parent[i] = j
#             self.size[j] += self.size[i]
#         else:
#             self.parent[j] = i
#             self.size[i] += self.size[j]

#     def is_connected(self, p, q):
#         return self.find(p) == self.find(q)
    

