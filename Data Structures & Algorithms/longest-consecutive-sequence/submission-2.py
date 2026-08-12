class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest = 1 if nums else 0
        for num in nums:
            if (num - 1) not in nums_set:
                # num can be a potential start
                potential_longest = 1
                next_num = num + 1
                while next_num in nums_set:
                    potential_longest += 1
                    next_num += 1
                    longest = max(longest, potential_longest)
                
                else:
                    continue
        return longest