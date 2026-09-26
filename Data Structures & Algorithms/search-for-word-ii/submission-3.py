class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
        self.index = None


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word, index):
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.end = True
        curr.index = index


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        rows = len(board)
        cols = len(board[0])
        tree = Trie()
        for idx, word in enumerate(words):
            tree.insert(word, idx)

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        visited = set()
        res = set()

        def dfs(node, r, c):
            char = board[r][c]
            if char not in node.children:
                return False
            node = node.children[char]
            if node.end:
                res.add(words[node.index])
            visited.add((r, c))
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                    if dfs(node, nr, nc):
                        return True
            visited.remove((r, c))
            return False

        for i in range(rows):
            for j in range(cols):
                dfs(tree.root, i, j)
        return list(res)
