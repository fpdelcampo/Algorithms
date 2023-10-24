class Solution:
    # We basically want a decreasing contiguous subarray that ends at the last index
    # We also note that small buildings don't cause problems, but big buildings do

    def findBuildings(self, heights: List[int]) -> List[int]:
        # Attempt 1:
        # Time: O(n)
        # Space: O(n)
        # Description: Simple monotonic stack
        # stack = []
        # for i in range(len(heights)):
        #     while stack and heights[stack[-1]] <= heights[i]:
        #         stack.pop()
        #     stack.append(i)
        # return stack
        ans = []
        curr = 0
        for i in range(len(heights)-1, -1, -1):
            if heights[i] > curr:
                ans.append(i)
                curr = heights[i]
        return ans[::-1]