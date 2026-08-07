# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy
        carry = 0

        while l1 is not None or l2 is not None or carry:
            num1 = l1.val if l1 else 0
            num2 = l2.val if l2 else 0

            new_digit = (num1 + num2 + carry) % 10
            carry =  (num1 + num2 + carry) // 10

            curr.next = ListNode(new_digit)
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next
