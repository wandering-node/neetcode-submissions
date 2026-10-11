class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        finder = 0
        while finder != slow:
            slow = nums[slow]
            finder = nums[finder]
        return finder