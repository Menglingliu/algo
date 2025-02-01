import heapq

def dijkstra(myd, start):
    visited = set()
    pq = [(0, start)]
    ans = []
    while pq:
        dis, node = heapq.heappop(pq)
        if node in visited:
            continue
        ans.append((node, dis))
        visited.add(node)
        if node not in myd:
            continue
        for nxt, dis_extra in myd[node]:
            if nxt in visited:
                continue
            heapq.heappush(pq, (dis + dis_extra, nxt))
    return ans

myd = {'a': [('b', 1), ('c', 3)], 'b': [('d', 1), ('c', 1)], 'd': [('e', 3)]}
print(dijkstra(myd, 'a'))