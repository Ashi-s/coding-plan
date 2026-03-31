class CountSquares:

    def __init__(self):
        self.d = {}
        

    def add(self, point: List[int]) -> None:
        point = tuple(point)
        if point not in self.d:
            self.d[point] = 1
        else:
            self.d[point] += 1
        

    def count(self, point: List[int]) -> int:
        res = 0
        dx, dy = point

        for p, count in self.d.items():
            x, y = p

            if abs(dx-x) == abs(dy-y) and x != dx and y != dy:
                point1 = (x, dy)
                point2 = (dx, y)

                # forms squares
                if point1 in self.d and point2 in self.d:
                    res += self.d[point1] * self.d[point2] * self.d[(x,y)]
        
        return res