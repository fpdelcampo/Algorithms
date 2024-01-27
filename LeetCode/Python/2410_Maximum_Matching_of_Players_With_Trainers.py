class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        j = 0
        res = 0
        for i in range(len(players)):
            while j < len(trainers) and trainers[j] < players[i]:
                j += 1
            if j < len(trainers) and players[i] <= trainers[j]:
                j += 1
                res += 1
        return res