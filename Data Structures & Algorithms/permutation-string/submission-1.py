class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        tracker = [0] * 26
        for char in s1:
            tracker[ord(char)-ord('a')] += 1

        for i in range(len(s2)-len(s1)+1):
            tmp_str = s2[i:i+len(s1)]
            tmp_tracker = tracker.copy()
            for char in tmp_str:
                tmp_tracker[ord(char)-ord('a')] -= 1
            if tmp_tracker == [0] * 26:
                return True
        return False
