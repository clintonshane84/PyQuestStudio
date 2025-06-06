from typing import List, Tuple, Dict, Any


class Polygon:
    def __init__(self, points: List[Tuple[int, int]]):
        self.points = points  # List of (x, y) tuples

    def to_dict(self) -> Dict[str, Any]:
        return {
            "points": self.points
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]):
        return cls(points=[tuple(point) for point in data["points"]])

    def contains_point(self, x: int, y: int) -> bool:
        # Ray casting algorithm for polygon hit test (basic form)
        num = len(self.points)
        j = num - 1
        inside = False
        for i in range(num):
            xi, yi = self.points[i]
            xj, yj = self.points[j]
            if ((yi > y) != (yj > y)) and \
                    (x < (xj - xi) * (y - yi) / (yj - yi + 1e-10) + xi):
                inside = not inside
            j = i
        return inside
