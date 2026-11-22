class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.index = None
        self.end = False


class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, word, index):
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.index = index
        curr.end = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        rows = len(board)
        cols = len(board[0])
        tree = Trie()
        for idx, word in enumerate(words):
            tree.insert(word, idx)

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        visited = set()
        res = []

        def dfs(r, c, node):
            char = board[r][c]
            if char not in node.children:
                return
            node = node.children[char]
            if node.end:
                res.append(words[node.index])
                node.end = False
            visited.add((r, c))
            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                    dfs(nr, nc, node)
            visited.remove((r, c))

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, tree.root)
        return res
