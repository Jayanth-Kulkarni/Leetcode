# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        res = []
        def dfs(root):
            if not root:
                res.append("N")
                return
            
            res.append(str(root.val))
            dfs(root.left)
            dfs(root.right)

            return
        dfs(root)
        return ",".join(res)

    def deserialize(self, data):
        data = data.split(",")
        self.i = 0
        def dfs():
            if self.i < len(data) and data[self.i] == "N":
                self.i += 1
                return None
            
            node = TreeNode(data[self.i]) 
            self.i += 1
            node.left = dfs()
            node.right = dfs()

            return node
        return dfs()

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))