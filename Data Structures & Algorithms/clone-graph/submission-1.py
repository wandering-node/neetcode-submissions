"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        mapping = {}
        def clone(node):
            if not node:
                return
            if node in mapping:
                return mapping[node]
            new_node = Node(node.val)
            mapping[node] = new_node
            for nei in node.neighbors:
                new_node.neighbors.append(clone(nei))
            return new_node
        return clone(node)