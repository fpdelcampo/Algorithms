class Solution:
    # Observation: we can get at most len(tokens)
    # When do we play face up or down?
    # We should probably play the highest ones face down
    # What order should we go in?
    # We sort in increasing order
    # Play first one face up to get a score of 1
    # Keep playing face up until we get tokens[i] < power
    # Then, *try* to play tokens[-1] down with the idea of being able to play more face-up.  (Basically, need to have something to track "attempts")
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        res = 0
        tokens.sort()
        if not tokens:
            return 0
        if power < tokens[0]:
            return 0
        l = 0
        r = len(tokens) - 1
        last = False
        while l <= r:
            last = False
            if tokens[l] <= power:
                power -= tokens[l]
                res += 1
                l += 1
                
            else:
                power += tokens[r]
                res -= 1
                r -= 1
                last = True
        if last:
            res += 1
        return res