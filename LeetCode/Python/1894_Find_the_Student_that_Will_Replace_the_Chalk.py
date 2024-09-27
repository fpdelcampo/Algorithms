class Solution:
    # Basically, we want "reduce" k until it is between 0...sum(chalk)
    
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        s = sum(chalk)
        target = k % s
        for i in range(len(chalk)):
            if target < chalk[i]:
                return i
            target -= chalk[i]
        return len(chalk) - 1