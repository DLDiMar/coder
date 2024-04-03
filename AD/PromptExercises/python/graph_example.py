def add_edge(graph, source, dest):
    """Adds an edge to the graph.

    Args:
        graph: A dictionary representing the graph.
        source: The source node of the edge.
        dest: The destination node of the edge.
    """
    if source in graph:
        graph[source].append(dest)
    else:
        graph[source] = [dest]

    # For undirected graphs, add the edge in both directions
    if dest not in graph:
        graph[dest] = []
    graph[dest].append(source)


def find_all_paths(graph, start, end, path=[]):
    """Finds all paths between two nodes in a graph (using depth-first search).

    Args:
        graph: A dictionary representing the graph.
        start: The starting node of the path.
        end: The ending node of the path.
        path: An optional list to store the current path.

    Returns:
        A list of all paths between start and end.
    """
    path = path + [start]
    if start == end:
        return [path]
    if start not in graph:
        return []

    paths = []
    for node in graph[start]:
        if node not in path:
            new_paths = find_all_paths(graph, node, end, path)
            for p in new_paths:
                paths.append(p)

    return paths


def find_shortest_path(graph, start, end):
    """Finds the shortest path between two nodes in a graph (using breadth-first search).

    Args:
        graph: A dictionary representing the graph.
        start: The starting node of the path.
        end: The ending node of the path.

    Returns:
        The shortest path between start and end, or None if no path exists.
    """
    queue = [(start, [start])]  # Store pairs of (node, path)
    visited = set()

    while queue:
        (node, path) = queue.pop(0)
        if node not in visited:
            visited.add(node)

            if node == end:
                return path

            for neighbor in graph[node]:
                if neighbor not in visited:
                    new_path = path + [neighbor]
                    queue.append((neighbor, new_path))

    return None


def has_path_of_length(graph, start, end, length, path=[]):
    """Checks if there exists a path of a specific length, short-circuiting.

    Args:
        graph: A dictionary representing the graph.
        start: The starting node of the path.
        end: The ending node of the path.
        length: The desired length of the path.
        path: An optional list to store the current path.

    Returns:
        True if a path of the specified length exists, False otherwise.
    """
    path = path + [start]

    if len(path) == length + 1:  # +1 to account for the starting node
        return start == end

    if start not in graph:
        return False

    for node in graph[start]:
        if node not in path and has_path_of_length(graph, node, end, length, path):
            return True  # Short-circuit as soon as a path is found

    return False


# Example usage
if __name__ == "__main__":
    graph = {}
    add_edge(graph, 'A', 'B')
    add_edge(graph, 'A', 'C')
    add_edge(graph, 'B', 'D')
    add_edge(graph, 'C', 'D')
    add_edge(graph, 'C', 'E')
    add_edge(graph, 'D', 'E')

    print("All paths from A to E:", find_all_paths(graph, 'A', 'E'))
    print("Shortest path from A to E:", find_shortest_path(graph, 'A', 'E'))

    node_1 = 'A'
    node_2 = 'D'
    path_length = 1
    if has_path_of_length(graph, node_1, node_2, path_length):
        print(f"A path of length {path_length} exists from {node_1} to {node_2}")
    else:
        print(f"No path of length {path_length} exists from {node_1} to {node_2}")