# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        if not root:
            return []
        queue.append([root])
        result = [[root.val]]
        while(len(queue)>0):
            inner_queue, inner_value = [], []
            queue_list = queue.popleft()
            for ele in queue_list:
                if ele.right != None and ele.left != None:
                    inner_value.append(ele.left.val)
                    inner_value.append(ele.right.val)
                    inner_queue.append(ele.left)
                    inner_queue.append(ele.right)
                elif ele.right != None:
                    inner_value.append(ele.right.val)
                    inner_queue.append(ele.right)
                elif ele.left != None:
                    inner_value.append(ele.left.val)
                    inner_queue.append(ele.left)
            if inner_value != []:
                queue.append(inner_queue)
                result.append(inner_value)
        return result