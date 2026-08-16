class Solution:
    def isValid(self, s: str) -> bool:
        rights = {'}': '{', ']': '[', ')': '('}
        stack = []
        for char in s:
            if char not in rights:
                stack.append(char)
            else:
                if stack:
                    if stack.pop() != rights[char]:
                        return False
                else:
                    return False
        if not stack:
            return True
        else:
            return False