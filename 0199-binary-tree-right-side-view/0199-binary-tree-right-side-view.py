# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        q = deque()
        q.append([root])
        res = [root.val]
        while q:
            inner = []
            innerval = []
            level = q.popleft()
            for node in level:
                if node.left:
                    inner.append(node.left)
                    innerval.append(node.left.val)
                if node.right:
                    inner.append(node.right)
                    innerval.append(node.right.val)
            if inner != []:
                q.append(inner)
                res.append(innerval[-1])
        return res