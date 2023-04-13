from typing import List

class Solution:
    def isRectangleOverlap(self, rect1: List[int], rect2: List[int]) -> bool:
        ax1, ay1, ax2, ay2 = rect1
        bx1, by1, bx2, by2 = rect2
        return self.intervalOverlap(ax1, ax2, bx1, bx2) and self.intervalOverlap(ay1, ay2, by1, by2)

    def intervalOverlap(self, x, y, k, j):
        return j > x > k or y > k > x or k < y < j or y > j > x
