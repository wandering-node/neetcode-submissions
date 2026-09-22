class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
        self.index = None

class PrefixTree:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str, index: int) -> None:
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
        directions = [
            [0, 1],
            [0, -1],
            [1, 0],
            [-1, 0]
        ]
        tree = PrefixTree()
        for idx, word in enumerate(words):
            tree.insert(word, idx)
        res = []
        visited = set()

        def dfs(node, r, c):
            char = board[r][c]
            if char not in node.children:
                return
            node = node.children[char]
            if node.end:
                res.append(words[node.index])
                node.end = False
            
            visited.add((r, c))
            for dr, dc in directions:
                new_r, new_c = r + dr, c + dc
                if 0 <= new_r < rows and 0 <= new_c < cols and (new_r, new_c) not in visited:
                    dfs(node, new_r, new_c)
            visited.remove((r, c))

        for row in range(rows):
            for col in range(cols):
                dfs(tree.root, row, col)
        return res