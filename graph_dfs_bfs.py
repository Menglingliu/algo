import collections

# ----------------------------------------------------------------------------------------------------
# DFS search on a graph starting with node: Recursive approach
def dfs_rec(graph, node, visited):
    ans = []
    ans.append(node) # exit criteria
    visited.add(node)
    for nxt in graph[node]:
        if nxt not in visited:
            #visited.add(nxt)
            ans += dfs_rec(graph, nxt, visited)
    return ans


def dfs_rec_1(graph, node):
    visited = set()
    ans = []
    def dfs_helper(node):
        ans.append(node) # exit criteria
        visited.add(node)
        for nxt in graph[node]:
            if nxt not in visited:
                dfs_helper(nxt)
        return ans
    return dfs_helper(node)


# DFS search on a graph starting with root: Iterative approach
def dfs(graph, root):
    ans = []
    stack = [root]
    visited = set([root])
    while stack:
        node = stack.pop()
        ans.append(node)
        for nxt in graph[node]:
            if nxt not in visited:
                stack.append(nxt)
                visited.add(nxt)                
    return ans

# ----------------------------------------------------------------------------------------------------
# BFS search on a graph starting with root: Iterative approach
def bfs(graph, root):
    ans = []
    queue = collections.deque([root])
    visited = set([root])
    while queue:
        node = queue.popleft()
        ans.append(node)
        for nxt in graph[node]:
            if nxt not in visited:
                queue.append(nxt)
                visited.add(nxt)
    return ans

# ----------------------------------------------------------------------------------------------------
# Test cases

graph_0 = {
    "a": set(["b", "c"]), 
    "b": set(["c", "a", "d"]), 
    "c": set(["a", "b"]), 
    "d": set(["b"])
}

graph_1 = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

graph_2 = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}


# DFS
visited = set()
print(dfs_rec(graph_1, 'A', visited))

print(dfs_rec_1(graph_1, 'A'))

print(dfs(graph_1, 'A'))

# BFS
print(bfs(graph_2, 'A'))

# DFS
# assert dfs_rec(graph_1, 'A', visited) == ['A', 'B', 'D', 'E', 'F', 'C'] 
# assert dfs(graph_1, 'A') == ['A', 'C', 'F', 'E', 'B', 'D']

# BFS
# assert bfs(graph_1, 'A') == ['A', 'B', 'C', 'D', 'E', 'F']


# ----------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------

# # DFS problems
# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
        
#         def dfs(i, j):
#             stack = [(i,j)]
#             grid[i][j] = '2'
#             while stack:
#                 r, c = stack.pop()
#                 for (dr, dc) in [(0,1), (1,0), (0,-1), (-1,0)]:
#                     r_nxt, c_nxt = r + dr, c + dc
#                     if r_nxt in range(n) and c_nxt in range(m) and grid[r_nxt][c_nxt] == '1':
#                         stack.append((r_nxt, c_nxt)) 
#                         grid[r_nxt][c_nxt] = '2'

#         n, m = len(grid), len(grid[0])
#         count = 0
#         for i in range(n):
#             for j in range(m):
#                 if grid[i][j] == '1':
#                     dfs(i, j)
#                     count += 1
#         return count



# # BFS problems
# class Solution:
#     def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
#         m, n = len(maze), len(maze[0])
#         queue = deque()
#         queue.append([entrance[0], entrance[1], 0])
#         maze[entrance[0]][entrance[1]] = '+'
        
#         while queue:
#             row, col, distance = queue.popleft()
            
#             if (row == 0 or row == m-1 or col == 0 or col == n-1) and distance > 0:
#                 return distance
            
#             directions = [(1,0), (0,1), (-1,0), (0,-1)]
#             for dr, dc in directions:
#                 r, c = row + dr, col + dc
#                 if r in range(m) and c in range(n) and maze[r][c] == '.':
#                     maze[r][c] = '+'
#                     queue.append([r, c, distance + 1])
#         return -1 