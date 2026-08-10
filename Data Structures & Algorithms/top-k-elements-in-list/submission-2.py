class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        # get frequency of each number in nums
        count = Counter(nums)
        # initialize a frequency map for each frequency
        # length of the map if len(nums) + 1 as no number can appear more than len(nums) in the original nums list. + 1 is for the index sake
        freq_map = [[] for _ in range(len(nums) + 1)]
        # loop through count to update the freq_map so that each sub-list at index i is the numbers that appeared i times in nums
        for num, freq in count.items():
            freq_map[freq].append(num)

        # now loop through freq_map from the most frequent ones to the least
        ans = []
        for i in range(len(freq_map) - 1, 0, -1):
            if len(ans) == k:
                return ans
            else:
                ans.extend(freq_map[i])
        return ans
