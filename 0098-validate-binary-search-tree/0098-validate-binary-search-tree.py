# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(min_val, max_val, root):
            if not root:
                return True

            if not (min_val < root.val < max_val):
                return False
            
            return dfs(min_val, root.val, root.left) and dfs(root.val, max_val, root.right)
        
        return dfs(float("-inf"), float("inf"), root)