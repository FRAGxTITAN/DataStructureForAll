class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        rootX, rootY = self.find(x), self.find(y)
        if rootX != rootY:
            self.parent[rootY] = rootX
            return True
        return False

def kruskal(n, edges):
    edges.sort(key=lambda x: x[2])  # sort by weight
    ds = DisjointSet(n)
    mst = []
    total_weight = 0

    for u, v, w in edges:
        if ds.union(u, v):
            mst.append((u, v, w))
            total_weight += w
    
    return mst, total_weight


# Example
edges = [(0,1,10),(0,2,6),(0,3,5),(1,3,15),(2,3,4)]
mst, weight = kruskal(4, edges)
print("MST:", mst)
print("Total Weight:", weight)
