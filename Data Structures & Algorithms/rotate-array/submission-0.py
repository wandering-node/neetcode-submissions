class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        old = nums.copy()
        for i, num in enumerate(old):
            new_idx = (i + k) % len(nums)
            nums[new_idx] = num
        