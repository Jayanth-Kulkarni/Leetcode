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
        res = [root.val]
        while queue:
            level = queue.popleft()
            inner_res = []
            inner_val = []
            for i in range(len(level)):
                if level[i].left:
                    inner_val.append(level[i].left.val)
                    inner_res.append(level[i].left)
                if level[i].right:
                    inner_val.append(level[i].right.val)
                    inner_res.append(level[i].right)
            if inner_val != []:
                print(inner_res)
                queue.append(inner_res)
                res.append(inner_val[-1])

        return res