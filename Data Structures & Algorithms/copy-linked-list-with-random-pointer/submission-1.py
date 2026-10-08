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
        deep_copy = {None: None} # deep copy is a dictionary whose key is the old node and the value is the new node
        curr = head

        while curr:
            deep_copy[curr] = Node(curr.val)
            curr = curr.next
        
        curr = head
        while curr:
            copied = deep_copy[curr]
            copied_next = deep_copy[curr.next]
            copied_rand = deep_copy[curr.random]
            copied.next, copied.random = copied_next, copied_rand
            curr = curr.next
        
        return deep_copy[head]