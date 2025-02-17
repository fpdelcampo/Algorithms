class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        count = 26 * [0]
        for tile in tiles:
            count[ord(tile) - ord('A')] += 1
        seen = set([])
        def solve(curr):
            nonlocal seen
            nonlocal count
            for i in range(26):
                if count[i] > 0:
                    new = curr + chr(ord('A') + i)
                    count[i] -= 1
                    seen.add(new)
                    solve(new)
                    count[i] += 1
        solve("")
        return len(seen)