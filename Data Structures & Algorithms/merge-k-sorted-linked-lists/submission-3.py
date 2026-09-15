# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return
        def divide(left, right):
            if left == right:
                return lists[left]

            mid = (left + right) // 2
            left_list = divide(left, mid)
            right_list = divide(mid + 1, right)
            return merge(left_list, right_list)
        def merge(l1, l2):
            dummy = ListNode(0)
            curr = dummy
            while l1 and l2:
                if l1.val < l2.val:
                    curr.next = l1
                    l1 = l1.next
                else:
                    curr.next = l2
                    l2 = l2.next
                curr = curr.next
            if l1:
                curr.next = l1
            if l2:
                curr.next = l2
            return dummy.next
        return divide(0, len(lists) - 1)

            