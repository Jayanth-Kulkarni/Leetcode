"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        clone = {}
        def dfs(node):
            if not node:
                return None
            
            if node in clone:
                return clone[node]
            
            duplicate = Node(node.val)
            clone[node] = duplicate

            for nei in node.neighbors:
                clone[node].neighbors.append(dfs(nei))
            
            return clone[node]
        return dfs(node)
    

