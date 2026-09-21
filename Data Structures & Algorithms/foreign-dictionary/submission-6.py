class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {char: set() for word in words for char in word}
        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i + 1]
            minLen = min(len(word1), len(word2))
            if len(word1) > len(word2) and word1[:minLen] == word2[:minLen]:
                return ""
            for j in range(minLen):
                if word1[j] != word2[j]:
                    adj[word1[j]].add(word2[j])
                    break
            
        visited = {} # not existed means not touched yet, False means visited with no circle, True means is visiting
        res = [] # append each valid character into the result list
        def dfs(char):
            if char in visited:
                return visited[char]
            visited[char] = True
            for nei in adj[char]:
                if dfs(nei):
                    return True
            visited[char] = False
            res.append(char)
            return False

        for char in adj:
            if dfs(char):
                return ""
        res.reverse()
        return "".join(res) 
