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
        visited = set()
        result = [[root.val]]
        while len(queue) > 0:
            inner_queue = []
            inner_value = []
            queue_list = queue.pop(0)
            for cur in queue_list:
                if cur.left != None:
                    inner_queue.append(cur.left)
                    inner_value.append(cur.left.val)
                if cur.right != None:
                    inner_queue.append(cur.right)
                    inner_value.append(cur.right.val)
            if inner_queue != []:
                queue.append(inner_queue)
                result.append(inner_value)
        return result