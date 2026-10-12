class Solution:
    def checkValidString(self, s: str) -> bool:
        left_stack = []
        star_stack = []
        for idx, char in enumerate(s):
            if char == '(':
                left_stack.append(idx)
            elif char == '*':
                star_stack.append(idx)
            else:
                if left_stack:
                    left_stack.pop()
                elif star_stack:
                    star_stack.pop()
                else:
                    return False

        while left_stack and star_stack:
            left = left_stack.pop()
            right = star_stack.pop()
            if left > right:
                return False
        if left_stack:
            return False
        
        return True