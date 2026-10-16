class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        count = Counter(hand)
        for num in sorted(hand):
            if count[num] != 0:
                for i in range(groupSize):
                    curr = num + i
                    # print(curr, count[curr])
                    if curr in count and count[curr] > 0:
                        count[curr] -= 1
                    else:
                        return False
        return True