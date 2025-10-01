def tarjans_scc(graph):
    n = len(graph)
    index = [None]*n
    lowlink = [None]*n
    stack, on_stack = [], [False]*n
    sccs = []
    idx = 0

    def strongconnect(v):
        nonlocal idx
        index[v] = lowlink[v] = idx
        idx += 1
        stack.append(v)
        on_stack[v] = True

        for w in graph[v]:
            if index[w] is None:
                strongconnect(w)
                lowlink[v] = min(lowlink[v], lowlink[w])
            elif on_stack[w]:
                lowlink[v] = min(lowlink[v], index[w])

        if lowlink[v] == index[v]:
            scc = []
            while True:
                w = stack.pop()
                on_stack[w] = False
                scc.append(w)
                if w == v:
                    break
            sccs.append(scc)

    for v in range(n):
        if index[v] is None:
            strongconnect(v)

    return sccs


# Example
graph = {
    0:[1], 1:[2], 2:[0,3], 3:[4], 4:[5,7], 5:[6], 6:[4], 7:[8], 8:[7]
}
print("SCCs:", tarjans_scc(graph))
