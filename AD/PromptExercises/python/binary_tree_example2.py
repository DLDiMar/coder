class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def breadth_first_search(self):
        """Performs a breadth-first search on the binary tree"""
        if self.root is None:
            return

        queue = [self.root]
        result = []

        while queue:
            node = queue.pop(0)
            result.append(node.data)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return result

    def depth_first_search(self):
        """Performs a depth-first search (in-order traversal) on the binary tree"""
        if self.root is None:
            return []

        stack = []
        result = []
        node = self.root

        while node or stack:
            while node:
                stack.append(node)
                node = node.left

            node = stack.pop()
            result.append(node.data)
            node = node.right

        return result

    def find_duplicates(self, data):
        """Counts occurrences of a value in the tree"""
        count = 0

        def _traverse(node):
            nonlocal count
            if node:
                if node.data == data:
                    count += 1
                _traverse(node.left)
                _traverse(node.right)

        _traverse(self.root)
        return count

    def find_childless_nodes(self):
        """Returns a list of values belonging to nodes with no children"""
        childless = []

        def _traverse(node):
            if node:
                if not node.left and not node.right:
                    childless.append(node.data)
                _traverse(node.left)
                _traverse(node.right)

        _traverse(self.root)
        return childless


# Example usage
tree = BinaryTree()
# ... (add nodes to your tree)
tree.root = Node(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)

print("Breadth-First Search:", tree.breadth_first_search())
print("Depth-First Search:", tree.depth_first_search())
print("Duplicates of 5:", tree.find_duplicates(5))  # Replace 5 with a value to search for
print("Childless Nodes:", tree.find_childless_nodes())