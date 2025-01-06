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
            if node in cloned:
                return cloned[node]
            
            if node == None:
                return None
            
            clone = Node(node.val)
            cloned[node] = clone
            for neighbours in node.neighbors:
                clone.neighbors.append(dfs(neighbours))
            
            return cloned[node]
        return dfs(node)