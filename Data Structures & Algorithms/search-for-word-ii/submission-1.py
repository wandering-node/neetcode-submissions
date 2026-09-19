class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False
        self.index = None


class PrefixTree:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str, index: int) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.endOfWord = True
        curr.index = index


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        tree = PrefixTree()
        for idx, word in enumerate(words):
            tree.insert(word, idx)
        res = []

        rows = len(board)
        cols = len(board[0])

        direcs = [
            [0, 1],
            [0, -1],
            [1, 0],
            [-1, 0]
        ]

        visited = set()

        def dfs(node, r, c):
            # 1. Check whether current character exists in Trie
            char = board[r][c]

            if char not in node.children:
                return
            
            # 2. Move Trie pointer forward
            node = node.children[char]

            # 3. We found a word
            if node.endOfWord:
                res.append(words[node.index])
                # prevent finding the same word again
                node.endOfWord = False

            # 4. Mark current board cell
            visited.add((r, c))

            # 5. Explore neighbors
            for dr, dc in direcs:
                new_r = r + dr
                new_c = c + dc

                if (
                    0 <= new_r < rows
                    and 0 <= new_c < cols
                    and (new_r, new_c) not in visited
                ):
                    dfs(node, new_r, new_c)

            # 6. Backtrack
            visited.remove((r, c))


        for row in range(rows):
            for col in range(cols):
                dfs(tree.root, row, col)
        return res
