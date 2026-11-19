"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from collections import deque


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        if not node:
            return
        clone_map = {}
        visited = set()
        queue = deque([node])
        while queue:
            curr = queue.popleft()
            if curr not in visited:
                new_node = Node(val=curr.val)
                clone_map[curr] = new_node
                queue.extend(curr.neighbors)
                visited.add(curr)
        
        queue = deque([node])
        visited = set()
        while queue:
            curr = queue.popleft()
            if curr not in visited:
                new_node = clone_map[curr]
                for nei in curr.neighbors: 
                    new_node.neighbors.append(clone_map[nei])
                visited.add(curr)
                queue.extend(curr.neighbors)
        return clone_map[node]
            
