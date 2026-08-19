class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapp = {']': '[', ')': '(', '}': '{'}
        for char in s:
            if char not in mapp:
                stack.append(char)
            else:
                if (not stack) or (stack[-1] != mapp[char]):
                    return False
                elif stack[-1] == mapp[char]:
                    stack.pop()
        return len(stack) == 0