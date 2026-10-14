class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        ind_a = ind_b = ind_c = 0
        for a, b, c in triplets:
            if a > target[0] or b > target[1] or c > target[2]:
                continue
            else:
                if not ind_a and a == target[0]:
                    ind_a = 1
                if not ind_b and b == target[1]:
                    ind_b = 1
                if not ind_c and c == target[2]:
                    ind_c = 1
        return bool(ind_a * ind_b * ind_c)         

