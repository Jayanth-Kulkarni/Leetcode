"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    clone = {}
    
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        if node in self.clone:
            return self.clone[node]
        
        copy = Node(node.val)
        self.clone[node] = copy

        for nei in node.neighbors:
            self.clone[node].neighbors.append(self.cloneGraph(nei))
        
        return self.clone[node]
    