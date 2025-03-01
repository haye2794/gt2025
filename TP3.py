import numpy as np
from collections import deque

# Construct adjacency matrix using numpy
def construct_adj_matrix(edges, num_nodes):
    adj_matrix = np.zeros((num_nodes, num_nodes), dtype=int)
    for u, v in edges:
        if 1 <= u <= num_nodes and 1 <= v <= num_nodes:
            adj_matrix[u - 1, v - 1] = 1  # Directed Graph
        else:
            print(f"Invalid edge: ({u}, {v})")
    return adj_matrix

# Define TreeNode class
class TreeNode:
    def __init__(self, label):
        self.label = label
        self.left = None
        self.right = None

# Iterative inorder traversal using a stack
def inorder_traversal(root):
    stack, result = [], []
    current = root
    while stack or current:
        if current:
            stack.append(current)
            current = current.left
        else:
            current = stack.pop()
            result.append(current.label)
            current = current.right
    return result

# Find subtree using BFS

def find_subtree(root, x):
    if not root:
        return None
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node.label == x:
            return node
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return None

if __name__ == "__main__":
    edges = [(1, 2), (1, 3), (2, 5), (2, 6), (3, 4), (4, 8), (5, 7)]
    num_nodes = 8
    adj_matrix = construct_adj_matrix(edges, num_nodes)
    print("a) Constructed Adjacency Matrix:")
    print(adj_matrix)
    
    # Construct tree
    root = TreeNode(1)
    root.left = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.left.left = TreeNode(8)
    root.right = TreeNode(2)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(5)
    root.right.right.left = TreeNode(7)
    
    # Get user input for inorder traversal
    x = int(input("b) Enter subtree root label for inorder traversal: "))
    subtree_root = find_subtree(root, x)
    
    if subtree_root:
        print(f"Inorder traversal of subtree rooted at node {x}: {inorder_traversal(subtree_root)}")
    else:
        print(f"Node {x} not found in the tree.")
