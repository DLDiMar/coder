class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

def breadth_first_search(root):
    if root is None:
        return []

    queue = [(root, 0)]  # Store nodes with their levels
    result = []
    while queue:
        node, level = queue.pop(0)
        result.append((node.value, level))
        for child in node.children:
            queue.append((child, level + 1))
    return result

def depth_first_search(root):
    if root is None:
        return []

    result = []
    stack = [(root, 0)]  # Store nodes with their levels
    while stack:
        node, level = stack.pop()
        result.append((node.value, level))
        for child in reversed(node.children):
            stack.append((child, level + 1))
    return result

def find_duplicates(root, value):
    if root is None:
        return 0

    count = 0
    if root.value == value:
        count += 1
    for child in root.children:
        count += find_duplicates(child, value)
    return count

def list_childless_nodes(root):
    if root is None:
        return []

    result = []
    if not root.children:
        result.append(root.value)
    for child in root.children:
        result += list_childless_nodes(child)
    return result

def largest_node_value(root):
    if root is None:
        return float('-inf'), -1  # Return negative infinity and -1 if empty tree

    max_value = float('-inf')
    max_level = -1
    queue = [(root, 0)]
    while queue:
        node, level = queue.pop(0)
        if node.value > max_value:
            max_value = node.value
            max_level = level
        for child in node.children:
            queue.append((child, level + 1))
    return max_value, max_level

def least_sum_path(root):
    if root is None:
        return 0, []  # Empty path has sum 0

    min_sum = float('inf')
    min_path = []

def least_sum_path(root):
    if root is None:
        return 0, []  # Return 0 (sum) and an empty path for an empty tree

    min_sum = float('inf')
    min_path = []

    def dfs_helper(node, current_sum, current_path):
        nonlocal min_sum, min_path  

        current_sum += node.value
        current_path.append(node.value)

        if not node.children:  # Leaf node
            if current_sum < min_sum:
                min_sum = current_sum
                min_path = current_path.copy()  # Make a copy of the path

        else:
            for child in node.children:
                dfs_helper(child, current_sum, current_path)

        current_path.pop()  # Backtrack

    dfs_helper(root, 0, [])
    return min_sum, min_path

# Example usage
if __name__ == "__main__":
    root = Node(15)
    root.children = [
        Node(10),
        Node(20),
        Node(15),
        Node(8),
        Node(25)
    ]
    root.children[1].children = [Node(18), Node(20)]

    print("BFS:", breadth_first_search(root))
    print("DFS:", depth_first_search(root))
    print("Duplicates of 15:", find_duplicates(root, 15))
    print("Childless nodes:", list_childless_nodes(root))
    print("Largest node:", largest_node_value(root))
    print("Least sum path:", least_sum_path(root))