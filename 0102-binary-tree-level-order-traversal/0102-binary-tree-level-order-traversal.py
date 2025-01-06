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
        queue = [[root]]
        result = [[root.val]]
        while len(queue) > 0:
            inner_vals = []
            inner_nodes = []
            current_nodes = queue.pop()
            for node in current_nodes:
                if node.left != None:
                    inner_vals.append(node.left.val)
                    inner_nodes.append(node.left)
                if node.right != None:
                    inner_vals.append(node.right.val)
                    inner_nodes.append(node.right)
            if inner_vals != []:
                result.append(inner_vals)
                queue.append(inner_nodes)
        return result
