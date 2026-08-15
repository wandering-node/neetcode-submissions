class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        all_nums = set(nums)
        length = 0
        for num in nums:
            if (num - 1) in all_nums:
                continue
            else:
                curr = num
                curr_length = 0
                while curr in all_nums:
                    curr_length += 1
                    curr += 1
                length = max(length, curr_length)
        return length

