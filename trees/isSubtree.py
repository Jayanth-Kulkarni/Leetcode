# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Split the problem into 2
# 1. DFS of the root tree.
# 2. While performing DFS do a isSameTree check for each node.
# Each node should go through the isSameTree check, don't add if conditions 
# Edge Cases in isSubtree
# * if not subRoot -> return true
# * After this check if not root -> false 
class Solution:
    def isSameTree(self,p: Optional[TreeNode], q:Optional[TreeNode]) -> bool:
        if (p==None or q==None) and p!=q:
            return False
        if p==None and q==None:
            return True
        if p.val!=q.val:
            return False

        return (self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right))

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False

        if self.isSameTree(root,subRoot):
            return True

        return (self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot))
