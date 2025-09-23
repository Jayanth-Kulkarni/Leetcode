# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(root, sum_till_node):
            if not root:
                return False
            
            sum_till_node += root.val

            if not root.left and not root.right:
                return sum_till_node == targetSum
            
            return dfs(root.left, sum_till_node) or dfs(root.right, sum_till_node)
        
        return dfs(root, 0)