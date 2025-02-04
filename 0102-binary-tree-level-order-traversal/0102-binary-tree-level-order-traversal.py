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

        while len(queue) > 0:
            level = queue.popleft()
            inner_list, inner_vals = [], []
            for node in level:
                if node.left:
                    inner_list.append(node.left)
                    inner_vals.append(node.left.val)
                if node.right:
                    inner_list.append(node.right)
                    inner_vals.append(node.right.val)
            if inner_list != []:
                res.append(inner_vals)
                queue.append(inner_list)
            
        return res
        