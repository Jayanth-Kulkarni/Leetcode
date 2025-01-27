# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def bfs(root, l, r):
            if not root:
                return True
    
            if not l < root.val < r:
                return False
            
            return (bfs(root.left, l, root.val) and bfs(root.right, root.val, r))

        return bfs(root, float("-inf"), float("inf"))