# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque()
        queue.append([root])
        res = [[root.val]]
        while queue:
            inner_val = []
            inner_queue = []
            for root in queue.popleft():
                if root.left:
                    inner_val.append(root.left.val)
                    inner_queue.append(root.left)
                if root.right:
                    inner_val.append(root.right.val)
                    inner_queue.append(root.right)
            if inner_val != []:
                queue.append(inner_queue)
                res.append(inner_val)        
        return res