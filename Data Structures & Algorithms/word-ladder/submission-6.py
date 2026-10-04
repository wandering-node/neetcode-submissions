class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        word_dict = collections.defaultdict(list)
        for word in wordList:
            for idx in range(len(word)):
                pattern = word[:idx] + "*" + word[idx + 1 :]
                word_dict[pattern].append(word)

        queue = collections.deque([(beginWord, 1)])
        while queue:
            curr, step = queue.popleft()
            if curr == endWord:
                return step
            for idx in range(len(curr)):
                pattern = curr[:idx] + "*" + curr[idx + 1 :]
                neighbors = word_dict.pop(pattern, [])
                for nei in neighbors:
                    queue.append((nei, step + 1))
        return 0


