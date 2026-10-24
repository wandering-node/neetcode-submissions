class CountSquares:
    def __init__(self):
        self.points = {}

    def add(self, point: List[int]) -> None:
        if tuple(point) in self.points:
            self.points[tuple(point)] += 1
        else:
            self.points[tuple(point)] = 1

    def count(self, point: List[int]) -> int:
        res = 0
        x1, y1 = point
        for x2, y2 in self.points.keys():
            if x1 == x2 and y1 == y2:
                continue
            elif (x2 - x1) == (y2 - y1) and (x1, y2) in self.points and (x2, y1) in self.points:
                res += self.points[(x1, y2)] * self.points[(x2, y1)] * self.points[(x2, y2)]
            elif (x1 + y1) == (x2 + y2) and (x1, y2) in self.points and (x2, y1) in self.points:
                res += self.points[(x1, y2)] * self.points[(x2, y1)] * self.points[(x2, y2)]
        return res
