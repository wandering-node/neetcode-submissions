class Solution:
    def checkValidString(self, s: str) -> bool:
        left = []
        star = []
        for idx, char in enumerate(s):
            if char == '(':
                left.append(idx)
            elif char == '*':
                star.append(idx)
            elif left:
                left.pop()
            elif star:
                star.pop()
            else:
                return False
        while left and star:
            left_idx = left.pop()
            star_idx = star.pop()
            if star_idx < left_idx:
                return False
        if left:
            return False
        return True
