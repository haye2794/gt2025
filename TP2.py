from collections import defaultdict, deque

def kosaraju_scc(graph, n):
    def dfs1(node):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs1(neighbor)
        stack.append(node)
    
    def dfs2(node, component):
        visited.add(node)
        component.append(node)
        for neighbor in transposed_graph[node]:
            if neighbor not in visited:
                dfs2(neighbor, component)
    
    # Step 1: DFS on original graph to fill stack
    visited = set()
    stack = []
    for i in range(n):
        if i not in visited:
            dfs1(i)
    
    # Step 2: Transpose the graph
    transposed_graph = defaultdict(list)
    for u in range(n):
        for v in graph[u]:
            transposed_graph[v].append(u)
    
    # Step 3: DFS on transposed graph to find SCCs
    visited.clear()
    sccs = []
    while stack:
        node = stack.pop()
        if node not in visited:
            component = []
            dfs2(node, component)
            sccs.append(set(component))
    
    return sccs

def find_wcc(graph, n):
    visited = set()
    wccs = []
    
    def bfs(start):
        queue = deque([start])
        component = set([start])
        visited.add(start)
        while queue:
            node = queue.popleft()
            for neighbor in undirected_graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    component.add(neighbor)
                    queue.append(neighbor)
        return component
    
    # Convert directed graph to undirected
    undirected_graph = defaultdict(set)
    for u in range(n):
        for v in graph[u]:
            undirected_graph[u].add(v)
            undirected_graph[v].add(u)
    
    # Find weakly connected components using BFS
    for i in range(n):
        if i not in visited:
            wccs.append(bfs(i))
    
    return wccs

def main():
    graph = {
        0: [1],
        1: [2, 5],
        2: [],
        3: [],
        4: [3, 6, 8],
        5: [2, 3],
        6: [2, 5, 7],
        7: [2, 8],
        8: []
    }
    n = len(graph)
    
    sccs = kosaraju_scc(graph, n)
    wccs = find_wcc(graph, n)
    
    print("Strongly Connected Components (SCCs):", sccs)
    print("Weakly Connected Components (WCCs):", wccs)

if __name__ == "__main__":
    main()
