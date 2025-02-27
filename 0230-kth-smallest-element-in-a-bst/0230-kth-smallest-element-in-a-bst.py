# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inOrderTraversal(self, root, order):
        if root:
            self.inOrderTraversal(root.left, order)
            order.append(root.val)
            self.inOrderTraversal(root.right, order)

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        order = []
        self.inOrderTraversal(root,order)
        return order[k-1]