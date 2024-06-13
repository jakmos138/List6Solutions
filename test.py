from collections import defaultdict

def detect_cycle_in_directed_graph(V, edges):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
    
    visited = [False] * V
    rec_stack = [False] * V
    
    def dfs(v):
        visited[v] = True
        rec_stack[v] = True
        
        for neighbor in graph[v]:
            if not visited[neighbor]:
                if dfs(neighbor):
                    return True
            elif rec_stack[neighbor]:
                return True
        
        rec_stack[v] = False
        return False
    
    for node in range(V):
        if not visited[node]:
            if dfs(node):
                return True
    return False

# Example usage:
V = 5
edges = [(0, 1), (1, 2), (2, 4), (2, 3)]
has_cycle = detect_cycle_in_directed_graph(V, edges)
print(f"Graph has a cycle: {has_cycle}")
