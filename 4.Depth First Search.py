def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start)
    for node in graph[start]:
        if node not in visited:
            dfs(graph, node, visited)

# Example usage:
graph = {
    'A': ['C', 'D'],
    'B': ['A', 'F'],
    'C': ['E'],
    'D': ['A'],
    'E': ['B','A'],
    'F': []
}

dfs(graph, 'C')