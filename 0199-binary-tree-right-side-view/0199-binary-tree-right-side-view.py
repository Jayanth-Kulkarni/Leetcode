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
        queue = deque()
        queue.append([root])
        res = []
        res.append(root.val)
        while len(queue) > 0:
            level = queue.popleft()
            inner_res = []
            inner_queue = []
            for i in range(len(level)):
                if level[i].left:
                    inner_queue.append(level[i].left)
                    inner_res.append(level[i].left.val)
                if level[i].right:
                    inner_queue.append(level[i].right)
                    inner_res.append(level[i].right.val)
            if inner_res != []:
                res.append(inner_res[-1])
                queue.append(inner_queue)
        return res