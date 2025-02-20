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
            length = len(level)
            inner_queue = []
            for i in range(length):
                node = level[i]
                if node.left:
                    inner_queue.append(node.left)
                if node.right:
                    inner_queue.append(node.right)
            if inner_queue != []:
                q.append(inner_queue)
                res.append(inner_queue[-1].val)
        return res