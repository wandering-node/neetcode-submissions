# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        first = head
        dummy = second = ListNode(0)
        second.next = head
        for i in range(n):
            first = first.next
        while first:
            second = second.next
            first = first.next
        tmp = second.next
        end = tmp.next if tmp else None
        second.next = end
        return dummy.next
        