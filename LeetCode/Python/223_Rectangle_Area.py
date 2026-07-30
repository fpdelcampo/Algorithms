# Just take area of both and then subtract the intersection
class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        a1 = abs(ax1 - ax2) * abs(ay1 - ay2)
        a2 = abs(bx1 - bx2) * abs(by1 - by2)
        overlap_width = max(0, min(ax2, bx2) - max(ax1, bx1))
        overlap_height = max(0, min(ay2, by2) - max(ay1, by1))
        return a1 + a2 - overlap_width * overlap_height