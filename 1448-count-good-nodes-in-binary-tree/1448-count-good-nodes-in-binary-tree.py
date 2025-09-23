# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def findgood(root, max_):
            if not root:
                return 0
            count = 0
            if root.val >= max_:
                count += 1
                max_ = root.val
            return findgood(root.left, max_) + findgood(root.right,max_) + count
        return findgood(root,float("-inf"))