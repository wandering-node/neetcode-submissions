class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        ord1 = [0] * 26
        ord2 = [0] * 26
        benchmark = ord('a')
        for i in range(len(s1)):
            ord1[ord(s1[i]) - benchmark] += 1
            ord2[ord(s2[i]) - benchmark] += 1
        if ord1 == ord2:
            return True
        for i in range(len(s1), len(s2)):
            ord2[ord(s2[i-len(s1)]) - benchmark] -= 1
            ord2[ord(s2[i]) - benchmark] += 1
            if ord1 == ord2:
                return True
        return False