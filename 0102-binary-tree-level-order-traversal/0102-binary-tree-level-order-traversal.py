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
        order = [[root.val]]
        while len(queue) > 0:
            roots = queue.popleft()
            inner_list = []
            inner_queue = []
            for root in roots:
                if root.left != None:
                    inner_list.append(root.left.val)
                    inner_queue.append(root.left)
                if root.right != None:
                    inner_list.append(root.right.val)
                    inner_queue.append(root.right)
            if inner_list != []: 
                order.append(inner_list)
                queue.append(inner_queue)
        return order