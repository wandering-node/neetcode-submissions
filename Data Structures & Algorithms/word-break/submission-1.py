class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * len(s)
        dp.append(True)
    
        len_s = len(s)
        for i in range(len_s - 1, -1, -1):
            for word in wordDict:
                len_w = len(word)
                if i + len_w <= len_s and s[i:i+len_w] == word:
                    dp[i] = dp[i+len_w]
                if dp[i]:
                    break
        return dp[0]



