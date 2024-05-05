from collections import deque  # Import deque from the collections module

# Define a function named bfs that performs breadth-first search (BFS) on a graph.
def bfs(graph, start):
    visited = set()  # Initialize a set to keep track of visited nodes
    queue = deque([start])  # Initialize a queue with the start node

    # Perform BFS while the queue is not empty
    while queue:
        node = queue.popleft()  # Get the first node from the queue
        if node not in visited:  # If the current node has not been visited
            print(node)  # Print the node (could be replaced with any other operation)
            visited.add(node)  # Mark the node as visited
            for neighbor in graph[node]:  # Iterate through the neighbors of the current node
                if neighbor not in visited:  # If the neighbor has not been visited
                    queue.append(neighbor)  # Add the neighbor to the queue

# Define the graph using a dictionary where keys are nodes and values are lists of neighbors.
graph = {
    'A': ['B', 'D'],  # Node A has neighbors B and D
    'B': ['D', 'F'],  # Node B has neighbors D and F
    'C': ['E'],       # Node C has neighbor E
    'D': ['C'],       # Node D has neighbor C
    'E': ['B'],       # Node E has neighbor B
    'F': []           # Node F has no neighbors
}

bfs(graph, 'A')  # Start BFS from node 'A'