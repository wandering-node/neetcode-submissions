class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        queue = collections.deque([])
        visited = set()
        fruit = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    queue.append((row, col))
                    visited.add((row, col))
                    fruit += 1
                elif grid[row][col] == 1:
                    fruit += 1
        if fruit == 0:
            return 0
        ans = 0
        while queue:
            ans += 1
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited and grid[nr][nc] == 1:
                        visited.add((nr, nc))
                        queue.append((nr, nc))
        
        if len(visited) == fruit:
            return ans - 1
        else:
            return -1
            
            
