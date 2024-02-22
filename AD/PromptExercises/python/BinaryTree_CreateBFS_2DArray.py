from collections import deque

def binary_tree_search(arr, target):
    # Validate input array
    if not arr or len(arr) == 0 or len(arr[0]) != 1:
        raise ValueError("Invalid input array")

    for i in range(1, len(arr)):
        if len(arr[i]) != 2 * len(arr[i - 1]):
            raise ValueError("Invalid input array")

    # Create a queue to store the nodes to be searched
    queue = deque([(0, 0)])  # Initialize with root node index and depth

    while queue:
        node_index, depth = queue.popleft()

        # If we've reached the target node
        if arr[depth][node_index] == target:
            return True

        # Add child nodes to the queue
        if depth < len(arr) - 1:
            # Get the child nodes from the next layer of the tree
            child_nodes = arr[depth + 1]
            for i in range(2 * node_index, 2 * node_index + 2):
                queue.append((i, depth + 1))

    return False  # If the target value is not found


arr = [
    [1],
    [2,3],
    [4,5,0,3],
    [4,7,1,2,4,8,10,8]
]

result = binary_tree_search(arr, 10)
print(result) # Should print True
