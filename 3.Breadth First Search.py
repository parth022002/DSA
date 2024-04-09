from collections import deque

def bfs(graph,start):
    visited  = set()
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node)
            visited.add(node)
            for neighbor in graph[node]:
                if  neighbor not in visited:
                    queue.append(neighbor)

#sample

graph = {
    'A': ['B', 'D'],
    'B': ['D', 'F'],
    'C': ['E'],
    'D': ['C'],
    'E': ['B'],
    'F': []
}

bfs(graph, 'A')