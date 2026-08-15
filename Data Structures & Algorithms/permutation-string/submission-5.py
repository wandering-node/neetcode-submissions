class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if (l2:=len(s2)) < (l1:=len(s1)):
            return False
        
        tracker1 = [0] * 26
        tracker2 = [0] * 26
        
        for i in range(l1):
            c1 = s1[i]
            c2 = s2[i]
            # get the tracker for s2
            tracker1[ord(c1) - ord('a')] += 1
            # get the tracker for the initial window in s2
            tracker2[ord(c2) - ord('a')] += 1
        if tracker2 == tracker1:
                return True
        
        for i in range(l1, l2):
            end = s2[i]
            start = s2[i-l1]
            tracker2[ord(end) - ord('a')] += 1
            tracker2[ord(start) - ord('a')] -= 1
            if tracker2 == tracker1:
                return True
        return False