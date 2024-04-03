class Node:
    def __init__(self, value):
        self.value = value
        self.children = []  # List to store children

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
    stack = [(root, 0)]
    while stack:
        node, level = stack.pop()
        result.append((node.value, level))
        for child in reversed(node.children):  # Reverse for DFS order
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
    if not root.children:  # Check if children list is empty
        result.append(root.value)
    for child in root.children:
        result += list_childless_nodes(child)
    return result

def largest_node_value(root):
    largest_value = float('-inf')  # Start with negative infinity
    largest_level = -1

    def helper(node, level):
        nonlocal largest_value, largest_level
        if node.value > largest_value:
            largest_value = node.value
            largest_level = level
        for child in node.children:
            helper(child, level + 1)

    helper(root, 0)
    return largest_value, largest_level

# Example usage (modify to create an n-ary tree)
if __name__ == "__main__":
    # Creating an example n-ary tree
    root = Node(1)
    child1 = Node(2)
    child2 = Node(3)
    child3 = Node(4)
    child4 = Node(5)
    child5 = Node(6)
    child6 = Node(7)
    child7 = Node(8)

    root.children = [child1, child2, child3]
    child1.children = [child4, child5]
    child2.children = [child6]
    child3.children = [child7]

    # Printing the tree structure
    print("Tree structure:")
    print("   1")
    print(" / | \\")
    print("2  3  4")
    print("/ \\  |")
    print("5 6  7 8")

    # Using the provided functions on the created tree
    print("\nBFS:", breadth_first_search(root))
    print("DFS:", depth_first_search(root))
    print("Duplicates of 2:", find_duplicates(root, 2))
    print("Childless nodes:", list_childless_nodes(root))
    largest, level = largest_node_value(root)
    print("Largest node value:", largest, "at level", level)
