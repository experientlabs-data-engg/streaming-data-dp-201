def valid_path(n: int, edges: list[list[int]], source: int, destination: int) -> bool:

    if source == destination:
        return True

    # Build the adjacency list representation of the graph
    adj_list = {i: [] for i in range(n)}
    print(adj_list)
    for u, v in edges:
        adj_list[u].append(v)
        adj_list[v].append(u)
    print(adj_list)
    # Perform Breadth-First Search (BFS)
    visited = [False] * n
    queue = [source]
    visited[source] = True

    while queue:
        curr = queue.pop(0)

        if curr == destination:
            return True

        for neighbor in adj_list[curr]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)

    return False

if __name__ == '__main__':
    n = 3
    edges = [[0, 1], [1, 2], [2, 0]]
    source = 0
    destination = 2
    print(valid_path(n, edges, source, destination))  # Output: True

    n = 6
    edges = [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]]
    source = 0
    destination = 5
    print(valid_path(n, edges, source, destination))  # Output: False