class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        arr = []
        for i in range(len(times)):
            arr.append([times[i][0], i])
            arr.append([times[i][1], -i])
        arr.sort()
        available = list(range(len(times)))
        occupied = []
        for event in arr:
            time, friend = event
            while occupied and occupied[0][0] <= time:
                _, chair = heapq.heappop(occupied)
                heapq.heappush(available, chair)  
            if friend >= 0:
                chair = heapq.heappop(available)
                if friend == targetFriend:
                    return chair
                heapq.heappush(occupied, [times[friend][1], chair])
        return -1
