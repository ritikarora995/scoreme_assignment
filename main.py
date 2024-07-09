"""
Assignment: Implement the most efficient algorithm to solve the given problem.

Problem Statement:
You are given a Directed Acyclic Graph (DAG) with `n` nodes, numbered from `0` to `n-1`.
The graph is represented as an adjacency list where `graph[i]` is a list of tuples `(j, w)`,
representing an edge from node `i` to node `j` with weight `w`. Your task is to find the longest
path in the graph starting from any node.

Function Signature:
def longest_path(graph: list) -> int:

Parameters:
- graph (list): A list of lists, where `graph[i]` contains tuples `(j, w)` representing an edge
  from node `i` to node `j` with weight `w`.

Returns:
- int: The length of the longest path in the graph.

Example:
>>> graph = [
...     [(1, 3), (2, 2)],
...     [(3, 4)],
...     [(3, 1)],
...     []
... ]
>>> longest_path(graph)
7
"""

from collections import deque

def longest_path(graph: list) -> int:
    n = len(graph)
    
    # Perform topological sort
    topo_order = topological_sort(graph)
    
    # Calculate the longest path using topological order
    return calculate_longest_path(graph, topo_order)

#  topological sort function
def topological_sort(graph):
    n = len(graph)
    in_degree = [0] * n
    for u in range(n):
        for v, _ in graph[u]:
            in_degree[v] += 1

    queue = deque([i for i in range(n) if in_degree[i] == 0])
    topo_order = []

    while queue:
        node = queue.popleft()
        topo_order.append(node)
        for neighbor, _ in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return topo_order

# Calculate longest path using topological sort
def calculate_longest_path(graph, topo_order):
    n = len(graph)
    dist = [-float('inf')] * n
    for i in range(n):
        dist[i] = 0

    for u in topo_order:
        for v, weight in graph[u]:
            if dist[v] < dist[u] + weight:
                dist[v] = dist[u] + weight

    return max(dist)


