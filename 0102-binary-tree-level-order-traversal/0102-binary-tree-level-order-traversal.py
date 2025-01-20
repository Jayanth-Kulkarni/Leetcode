# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
        queue = deque()
        queue.append([root])
        count = 0
        res = [[root.val]]
        while len(queue) > 0:
            level = queue.popleft()
            inner_val = []
            inner_level = []
            for node in level:
                if node.left != None:
                    inner_level.append(node.left)
                    inner_val.append(node.left.val)
                if node.right != None:
                    inner_level.append(node.right)
                    inner_val.append(node.right.val)
            if inner_val != []:
                res.append(inner_val)
                queue.append(inner_level)
        return res