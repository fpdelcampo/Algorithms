class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        # Player 1 should always win. Clearly, if player 1 can always win a game of size n - 4, then they can always win.  This is because player 1 should have a higher score after both player 1 and player 2 go.  Then since they have a higher score going into a game which they should always come out on top from, they will win.
        # Alternatively, we can see that player 1 can pick entirely even indices, or entirely odd indices. Since sum(piles[even]) != sum(piles[odd]), player 1 just chooses which ever one is larger and wins.
        return True
