class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def build_binary_tree(arr):
    if not arr:
        return None

    root = Node(arr[0])
    stack = [(root, 0)]

    while stack:
        node, index = stack.pop()
        left_index = 2 * index + 1
        right_index = 2 * index + 2

        if left_index < len(arr) and arr[left_index] is not None:
            node.left = Node(arr[left_index])
            stack.append((node.left, left_index))

        if right_index < len(arr) and arr[right_index] is not None:
            node.right = Node(arr[right_index])
            stack.append((node.right, right_index))

    return root

def print_tree(node, level=0, prefix="Root: "):
    if node is not None:
        if level == 0:
            print(prefix + str(node.value))
        else:
            print(" " * (level * 4 - 4) + prefix + str(node.value))
        if node.left is not None or node.right is not None:
            print_tree(node.left, level + 1, "L--- ")
            print_tree(node.right, level + 1, "R--- ")

# Define the array representing the binary tree
array = [0, 2, 4, 1, None, 3, -1, 5, 1, None, 6, None, 8]

# Create a binary tree from the array
root = build_binary_tree(array)

# Visualize the binary tree
print_tree(root)
