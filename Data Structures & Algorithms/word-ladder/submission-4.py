class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        word_dict = collections.defaultdict(list)
        for word in wordList:
            for idx in range(len(word)):
                key = word[:idx] + "*" + word[idx + 1 :]
                word_dict[key].append(word)
        queue = collections.deque([])
        for idx in range(len(beginWord)):
            key = beginWord[:idx] + "*" + beginWord[idx + 1 :]
            queue.append((key, 1))

        while queue:
            curr, step = queue.popleft()
            if curr in word_dict:
                if endWord in word_dict[curr]:
                    return step + 1
                for word in word_dict[curr]:
                    for idx in range(len(word)):
                        key = word[:idx] + "*" + word[idx + 1 :]
                        queue.append((key, step + 1))
                del word_dict[curr]
        return 0


