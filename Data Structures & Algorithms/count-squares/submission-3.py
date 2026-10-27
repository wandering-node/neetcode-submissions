class CountSquares:
    def __init__(self):
        self.points = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.points[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        x, y = point
        ans = 0
        for (nx, ny), cnt in self.points.items():
            if nx == x and ny == y:
                continue
            if (
                ((nx - x == ny - y) or (x + y == nx + ny))
                and (nx, y) in self.points
                and (x, ny) in self.points
            ):
                ans += self.points[(nx, y)] * self.points[(x, ny)] * cnt
        return ans
