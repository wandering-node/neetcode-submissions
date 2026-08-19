class Solution:
    def search(self, nums: List[int], target: int) -> int:
        mid_idx = len(nums) // 2
        l = 0
        r = len(nums) - 1
        while l <= r:
            if target > nums[mid_idx]:
                l = mid_idx + 1
                mid_idx = (l + r) // 2
            elif target < nums[mid_idx]:
                r = mid_idx - 1
                mid_idx = (l + r) // 2
            else:
                return mid_idx
        return -1
