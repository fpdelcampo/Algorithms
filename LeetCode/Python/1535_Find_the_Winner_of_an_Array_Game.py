class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        dq = deque(arr)
        winners = defaultdict(lambda: 0)
        winner = -1
        most = -1
        highest = max(arr)
        while most < k:
            if highest == dq[0]:
                return highest
            if dq[0] > dq[1]:
                winner = dq[0]
                winners[winner] += 1
                x = dq.popleft()
                y = dq.popleft()
                dq.appendleft(x)
                dq.append(y)
            else:
                winner = dq[1]
                winners[winner] += 1
                x = dq.popleft()
                dq.append(x)
            most = max(most, winners[winner])
        return winner