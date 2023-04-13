from typing import List
from math import sqrt

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        return sorted(points, key=lambda e: sqrt(abs(e[0]) ** 2 + abs(e[1]) ** 2))[0:k]
