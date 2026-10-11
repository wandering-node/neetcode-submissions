"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return
        info = {None: None}
        curr = head
        while curr:
            info[curr] = Node(curr.val)
            curr = curr.next
        
        curr = head
        while curr:
            info[curr].next = info[curr.next]
            info[curr].random = info[curr.random]
            curr = curr.next
        return info[head]