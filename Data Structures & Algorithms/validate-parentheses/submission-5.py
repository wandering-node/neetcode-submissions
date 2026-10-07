class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapp = {']': '[', ')': '(', '}': '{'}
        for char in s:
            if char not in mapp:
                stack.append(char)
            else:
                if stack and stack[-1] == mapp[char]:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0