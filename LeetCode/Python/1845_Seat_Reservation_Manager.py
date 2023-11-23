# Ideas:
# We need to quickly access the ith spot
# We need to have some sort of "order"
# Can probably use a priority queue

class SeatManager:

    def __init__(self, n: int):
        self.heap = [i for i in range(1, n+1)]
        heapq.heapify(self.heap)

    def reserve(self) -> int:
        x = heapq.heappop(self.heap)
        return x
        
    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.heap, seatNumber)


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)