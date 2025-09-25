# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        self.max = 0
        def dfs(root):
            if not root:
                return 0

            left_length = dfs(root.left)
            right_length = dfs(root.right)

            left_val = right_val = 0

            if root.left and root.left.val == root.val:
                left_val = left_length + 1
            if root.right and root.right.val == root.val:
                right_val = right_length + 1

            self.max = max(self.max, left_val + right_val)
            return max(left_val, right_val)

        dfs(root)
        return self.max