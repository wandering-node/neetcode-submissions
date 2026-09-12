# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def conquer(l1, l2):
            "leetcode easy: merge 2 lists"
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
        def divide(left, right):
            "divide into left and right sublists until we have 2 single lists to do the easy merge using conquer function"
            if left == right:
                return lists[left]
            mid = (left + right) // 2
            left_list = divide(left, mid)
            right_list = divide(mid + 1, right)
            return conquer(left_list, right_list)
        if not lists:
            return None

        return divide(0, len(lists) - 1)