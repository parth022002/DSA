# Define a function named depth_first_search that performs depth-first search (DFS) on a graph.
def depth_first_search(graph, start):
    visited = set()  # Initialize a set to keep track of visited nodes

    # Define a nested function dfs_recursive that performs DFS recursively from a given node.
    def dfs_recursive(node):
        if node not in visited:  # If the current node has not been visited
            visited.add(node)  # Mark the node as visited
            print(node)  # Print the node (could be replaced with any other operation)
            for neighbor in graph[node]:  # Iterate through the neighbors of the current node
                dfs_recursive(neighbor)  # Recursively call dfs_recursive on each neighbor

    dfs_recursive(start)  # Start DFS from the specified start node

# Example usage:
graph = {
    'A': ['C', 'D'],  # Node A has neighbors C and D
    'B': ['A', 'F'],  # Node B has neighbors A and F
    'C': ['E'],       # Node C has neighbor E
    'D': ['A'],       # Node D has neighbor A
    'E': ['B', 'A'],  # Node E has neighbors B and A
    'F': []           # Node F has no neighbors
}

depth_first_search(graph, 'C')  # Start DFS from node 'C'
