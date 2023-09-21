class Solution:
    # Use a greedy approach
    def minimumTime(self, jobs: List[int], workers: List[int]) -> int:
        jobs.sort()
        workers.sort()
        days = 0
        for i in range(len(jobs)):
            if jobs[i] % workers[i] == 0:
                days = max(days, jobs[i] // workers[i])
            else:
                days = max(days, jobs[i] // workers[i] + 1)
        return days