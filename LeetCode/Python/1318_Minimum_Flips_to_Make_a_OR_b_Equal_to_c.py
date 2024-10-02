# Idea:
# If a and b have a particular "on" bit that is "off" for c, we have to flip two bits
# If a or b have a particular "off" bit that is "on" for c, we have to flip it on
class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        return (a & (~c)).bit_count() + (b & (~c)).bit_count() + (~(a | b) & c).bit_count()