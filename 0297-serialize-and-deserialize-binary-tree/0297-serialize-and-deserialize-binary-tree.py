# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        self.l = []
        def dfs(node):
            if not node:
                self.l.append("N")
                return
            
            self.l.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
            return
        dfs(root)
        return ",".join(self.l)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        print(data)
        data = data.split(",")
        self.i = 0
        def dfs():
            if data[self.i] == "N":
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