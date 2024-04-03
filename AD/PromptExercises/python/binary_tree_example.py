class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def breadth_first_search(root):
    if root is None:
        return []

    queue = [root]
    result = []
    while queue:
        node = queue.pop(0)
        result.append(node.value)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result

def depth_first_search(root):
    if root is None:
        return []

    result = []
    stack = [root]
    while stack:
        node = stack.pop()
        result.append(node.value)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return result

def find_duplicates(root, value):
    if root is None:
        return 0

    count = 0
    if root.value == value:
        count += 1
    count += find_duplicates(root.left, value)
    count += find_duplicates(root.right, value)
    return count

def list_childless_nodes(root):
    if root is None:
        return []

    result = []
    if root.left is None and root.right is None:
        result.append(root.value)
    result += list_childless_nodes(root.left)
    result += list_childless_nodes(root.right)
    return result

# Example usage
if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(2)
    root.left.left = Node(3)
    root.left.right = Node(4)
    root.right.left = Node(4)

    print("BFS:", breadth_first_search(root))
    print("DFS:", depth_first_search(root))
    print("Duplicates of 2:", find_duplicates(root, 2))
    print("Childless nodes:", list_childless_nodes(root))