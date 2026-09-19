class TrieNode:
    def __init__(self):
        self.children = {}
        self.endIndicator = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        curr = self.root
        for s in word:
            if s not in curr.children:
                curr.children[s] = TrieNode()
            curr = curr.children[s]
        curr.endIndicator = True
        

    def search(self, word: str) -> bool:
        def dfs(index, node):
            if index == len(word):
                return node.endIndicator
            char = word[index]
            if char == '.':
                for child in node.children.values():
                    if dfs(index + 1, child):
                        return True
                return False
            if char not in node.children:
                return False
            return dfs(index + 1, node.children[char])

        return dfs(0, self.root)
