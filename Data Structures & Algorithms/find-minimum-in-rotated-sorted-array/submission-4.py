class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l+r) // 2
            # all sorted 
            if nums[l] <= nums[mid] and nums[mid] <= nums[r]:
                return nums[l]
            # left side sorted
            elif nums[l] <= nums[mid] and nums[mid] >= nums[r]:
                l = mid + 1
            # right side sorted
            elif nums[l] >= nums[mid] and nums[mid] <= nums[r]:
                r = mid
                     
        return nums[r]