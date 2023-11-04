# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 1. Use Iterative DFS (pre-order DFS)
# Since we are adding depth+1 to the stack, without checking if the node exists,
# We need to have a result variable that updates only if the node exists
class Solution:    
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        stack = [[root,1]]
        res=1
        while stack:
            root, depth = stack.pop()
            if root:
                res = max(depth,res)
                stack.append([root.left,depth+1])
                stack.append([root.right,depth+1])

        return res