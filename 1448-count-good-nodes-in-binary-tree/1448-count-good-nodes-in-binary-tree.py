class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0
        '''
        This function will update the self.count values if the path from root to X
        has not nodes with value greater than x, by getting the max_val arg that records 
        the current max value in the path.
        input: X, max_val 
        output: update the count and not return anything
        '''
        def dfs(X, max_val):
            if not X:
                return
            if X.val >= max_val:
                self.count += 1
            max_val = max(max_val, X.val)
            dfs(X.left, max_val)
            dfs(X.right, max_val)
            return
        dfs(root, root.val)
        return self.count