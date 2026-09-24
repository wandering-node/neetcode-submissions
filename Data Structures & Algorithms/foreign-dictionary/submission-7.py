class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        edges = {char: set() for word in words for char in word}
        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i + 1]
            minLen = min(len(word1), len(word2))
            if word1[:minLen] == word2[:minLen] and len(word1) > len(word2):
                return ""
            for j in range(minLen):
                if word1[j] != word2[j]:
                    edges[word1[j]].add(word2[j])
                    break
            
        visited = {}
        res = []
        def has_circle(char):
            if char in visited:
                return visited[char]
            visited[char] = True
            for nei in edges[char]:
                if has_circle(nei):
                    return True
            visited[char] = False
            res.append(char)
            return False
                
        for edge in edges:
            if has_circle(edge):
                return ''
        res.reverse()
        return "".join(res)