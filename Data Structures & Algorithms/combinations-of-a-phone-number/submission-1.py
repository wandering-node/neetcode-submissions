class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone_map = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }
        ans = []

        def backtrack(i, curr):
            if i == len(digits):
                ans.append("".join(curr))
                return
            for char in phone_map[digits[i]]:
                curr.append(char)
                backtrack(i + 1, curr)
                curr.pop()
        backtrack(0, [])
        return ans if digits else []