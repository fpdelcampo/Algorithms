class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        time = []
        for i in range(len(dist)):
            num = float(dist[i])
            denom = float(speed[i])
            t = ceil(num / denom)
            time.append(int(t))
        time.sort()
        for i in range(len(time)):
            if time[i] < i + 1:
                return i
        return len(time)