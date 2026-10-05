class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # heap = []
        # for num in nums:
        #     if len(heap) < k:
        #         heapq.heappush(heap, num)
        #     elif num > heap[0]:
        #         heapq.heapreplace(heap, num)
        # return heap[0]

        def divide(l, r):
            if l == r:
                return nums[l:r + 1]
            else:
                mid = (l + r) // 2
                left = divide(l, mid)
                right = divide(mid + 1, r)
                return conquer(left, right)

        def conquer(l1, l2):
            res = []
            i = j = 0
            while i < len(l1) and j < len(l2):
                if l1[i] > l2[j]:
                    res.append(l1[i])
                    i += 1
                else:
                    res.append(l2[j])
                    j += 1

            res.extend(l1[i:])
            res.extend(l2[j:])

            return res

        sort = divide(0, len(nums) - 1)
        return sort[k-1]