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
        cloned = {}
        def dfs(node):
            if not node:
                return None 
            if node in cloned:
                return cloned[node]

            clone = Node(node.val)
            cloned[node] = clone
            for nei in node.neighbors:
                clone.neighbors.append(dfs(nei))

            return cloned[node]
        
        return dfs(node)
        