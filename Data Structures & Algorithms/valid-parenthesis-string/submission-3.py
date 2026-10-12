class Solution:
    def checkValidString(self, s: str) -> bool:
        open_indices = []
        star_indices = []

        for i, char in enumerate(s):
            if char == "(":
                open_indices.append(i)
            elif char == "*":
                star_indices.append(i)
            elif open_indices:
                open_indices.pop()
            elif star_indices:
                star_indices.pop()
            else:
                return False

        # Each remaining '(' needs a '*' to its right.
        while open_indices and star_indices:
            if open_indices.pop() > star_indices.pop():
                return False

        return not open_indices
