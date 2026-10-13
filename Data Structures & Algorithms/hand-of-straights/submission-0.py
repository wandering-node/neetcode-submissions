class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        count =  Counter(hand)
        for start in sorted(hand):
            while count[start] > 0:
                for i in range(start, start + groupSize):
                    if count[i] == 0:
                        return False
                    count[i] -= 1
        return True