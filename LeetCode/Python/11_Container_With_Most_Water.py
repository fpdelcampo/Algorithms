class Solution:
    """
    
    See write up that I made, trick is the use of min in the computation of the height term for area

    """
    def maxArea(self, height: List[int]) -> int:
        best = -1
        l = 0
        r = len(height)-1
        while l<r:
            best = max(best, (r-l)*min(height[l], height[r]))
            if height[r]>height[l]:
                l+=1
            else:
                r-=1
        return best