class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        pattern_dict = collections.defaultdict(list)

        def get_keys(word):
            keys = []
            for idx in range(len(word)):
                key = word[:idx] + "*" + word[idx + 1 :]
                keys.append(key)
            return keys

        for word in wordList:
            keys = get_keys(word)
            for key in keys:
                pattern_dict[key].append(word)

        queue = collections.deque([])
        keys = get_keys(beginWord)
        queue.extend(keys)

        step = 1
        visited = set(beginWord)
        while queue:
            step += 1
            for _ in range(len(queue)):
                curr = queue.popleft()
                if endWord in pattern_dict[curr]:
                    return step 
                else:
                    for word in pattern_dict[curr]:
                        if word not in visited:
                            keys = get_keys(word)
                            queue.extend(keys)
                            visited.add(word)
                    pattern_dict[curr] = []
        return 0