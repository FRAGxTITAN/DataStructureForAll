def bellman_ford(n, edges, start):
    dist = [float("inf")] * n
    dist[start] = 0

    for _ in range(n-1):
        for u, v, w in edges:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    # Check negative cycle
    for u, v, w in edges:
        if dist[u] + w < dist[v]:
            return None  # Negative cycle detected

    return dist


# Example
edges = [(0,1,5),(1,2,-2),(0,2,4),(2,3,3)]
print("Bellman-Ford:", bellman_ford(4, edges, 0))
