# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.res = []
        self.inner = []
        def dfs(root, target):
            if not root:
                return 

            self.inner.append(root.val)
            if not root.left and not root.right:
                if target-root.val == 0:
                    self.res.append(self.inner[:])
                        
            left = dfs(root.left, target-root.val)
            right = dfs(root.right, target-root.val)

            self.inner.pop()
            return
            
        dfs(root,targetSum)
        return self.res