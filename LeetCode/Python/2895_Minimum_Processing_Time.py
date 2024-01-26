class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        tasks.sort()
        processorTime.sort(reverse = True)
        res = 0
        for i in range(len(processorTime)):
            res = max(res, processorTime[i] + tasks[4 * (i + 1) - 1])
        return res