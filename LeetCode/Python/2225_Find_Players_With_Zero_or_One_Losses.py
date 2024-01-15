class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        losses = {}
        winners = set()
        losers = set()
        for match in matches:
            x, y = match
            if x not in losses:
                losses[x] = 0
                winners.add(x)
            if y in losses:
                if y in winners:
                    winners.remove(y)
                losses[y] += 1
            else:
                if y in winners:
                    winners.remove(y)
                losses[y] = 1
            if losses[y] == 1:
                losers.add(y)
            elif losses[y] > 1 and y in losers:
                losers.remove(y)
        winners = list(winners)
        losers = list(losers)
        winners.sort()
        losers.sort()
        return [winners, losers]