class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        dx = abs(fx-sx)
        dy = abs(fy-sy)
        m = dx + dy - min(dx, dy)
        if sx == fx and sy == fy:
            return (t == 0) or (t > 1)
        if m > t:
            return False
        else:
            return True