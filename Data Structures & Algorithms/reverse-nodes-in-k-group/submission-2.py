# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        groupPrev = dummy = ListNode(0, head)
        while True:
            node = groupPrev
            for _ in range(k):
                node = node.next
                if not node:
                    return dummy.next
            groupNext = node.next

            nxt, curr = groupNext, groupPrev.next
            while curr != groupNext:
                tmp = curr.next
                curr.next = nxt
                nxt, curr = curr, tmp

            newTail = groupPrev.next  # old head is now the tail
            groupPrev.next = node  # kth is the new head of this group
            groupPrev = newTail  # tail becomes prev for the next group
