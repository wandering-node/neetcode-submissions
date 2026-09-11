# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head.next:
            return
        # first, using slow and fast pointers to find the middle of the list
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # print(slow.val, fast.val)
        # save the second half in a tmp variable
        prev = slow.next
        curr = prev.next
        prev.next = None
        # set the last element to the first half as None
        slow.next = None
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        # print(prev.val, prev.next.val, prev.next.next)
        dummy = ListNode(0)
        curr = dummy
        slow = head
        # print(slow.val, slow.next.val, slow.next.next)
        while slow and prev:
            curr.next = slow
            slow = slow.next
            curr = curr.next
            curr.next = prev
            prev = prev.next
            curr = curr.next
        if slow:
            curr.next = slow
        return 
