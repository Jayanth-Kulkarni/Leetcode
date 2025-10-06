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
        q = deque()
        q.append([root])
        res = [[root.val]]
        while q:
            current_level = q.pop()
            inner_list = []
            inner_nodes = []
            for node in current_level:
                if node.left:
                    inner_list.append(node.left.val)
                    inner_nodes.append(node.left)
                if node.right:
                    inner_list.append(node.right.val)
                    inner_nodes.append(node.right)
            if inner_list != [] or inner_nodes != []:
                res.append(inner_list)
                q.append(inner_nodes)
        return res