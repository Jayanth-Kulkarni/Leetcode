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
            level = q.popleft()
            inner_level = []
            inner_res = []
            for i in range(len(level)):
                node = level[i]
                if node.left != None:
                    inner_level.append(node.left)
                    inner_res.append(node.left.val)
                if node.right != None:
                    inner_level.append(node.right)
                    inner_res.append(node.right.val)

            if inner_level != []:
                res.append(inner_res[-1])
                q.append(inner_level)
        return res