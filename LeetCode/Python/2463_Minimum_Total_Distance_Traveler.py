# Intuition, we should probably sort everything, since in general robots should go to nearby factories
# One "pretty good" solution would be to have left most robot go to left most factory, etc.  This wouldn't directly work, since the the arrays can have different sizes, but you can think of, for exmaple, the factory entry [2, 3] as consisting of 3 entries of 2.
# Another thing to note is that the robot has to be serviced by the first available 
# 2D DP could work, but will be annoying to track factories that have hit their limit
# How to define relations? First sort.  Then, dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j] + |r[i] - f[j]|)
# For dp[i][j], we have to decide whether we put the ith robot with j-1th factory, or with the jth factory, and we use this cost function to figure that out
class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot = sorted(robot)
        factory = sorted(factory, key = lambda x : x[0])
        factories = []
        for i in range(len(factory)):
            tmp = [factory[i][0] for _ in range(factory[i][1])]
            factories.extend(tmp)
        dp = [[float('inf') for _ in range(len(factories) + 1)] for _ in range(len(robot) + 1)]
        dp[0] = [0 for _ in range(len(factories) + 1)] # If there are no robots, the cost is 0
        for i in range(1, len(robot) + 1):
            for j in range(1, len(factories) + 1):
                dp[i][j] = min(dp[i][j - 1], dp[i - 1][j - 1] + abs(robot[i - 1] - factories[j - 1]))
        return dp[-1][-1]