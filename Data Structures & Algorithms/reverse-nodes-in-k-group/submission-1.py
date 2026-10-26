# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr = head
        step = 0
        while curr and step < k:
            curr = curr.next
            step += 1

        if step == k:
            curr = self.reverseKGroup(curr, k)
            while step > 0:
                tmp = head.next
                head.next = curr
                curr = head
                head = tmp
                step -= 1
            head = curr
        return head
