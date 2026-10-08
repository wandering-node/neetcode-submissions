class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = 0
        while True:
            slow = nums[slow] # one step at a time.
            fast = nums[nums[fast]] # two steps at a time. 
            if slow == fast: # if these two pointers meet, we can guarantee that both pointers are inside the cycle caused by the duplicated number.
                break
        finder = 0
        while finder != slow:
            finder = nums[finder]
            slow = nums[slow]
        return finder