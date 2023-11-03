# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Use recursion to solve this problem
# First invert the left and right sub-trees
# Recursively call left and right sub-tree to be inverted
class Solution:
    def invertTree(self, root):
        if not root:
            return 

        temp = root.left
        root.left = root.right
        root.right = temp

        invertTree(root.left)
        invertTree(root.right)

        return root