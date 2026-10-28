class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2

        if len(A) > len(B):
            A, B = B, A

        m, n = len(A), len(B)
        left, right = 0, m
        half = (m + n + 1) // 2 # so that if the total elements is odd, we make sure the median is in the smaller half

        while left <= right:
            i = (left + right) //2 # number of elements from A to makeup for the smaller half
            j = half - i # number of elements from B to makeup for the smaller half

            Aleft = A[i - 1] if i > 0 else float("-inf")
            Aright = A[i] if i < m else float("inf")
            Bleft = B[j - 1] if j > 0 else float("-inf")
            Bright = B[j] if j < n else float("inf")

            if Aleft <= Bright and Bleft <= Aright:
                if (m + n) % 2 == 1:
                    return max(Aleft, Bleft)

                return (max(Aleft, Bleft) +
                        min(Aright, Bright)) / 2

            elif Aleft > Bright:
                right = i - 1
            else:
                left = i + 1