# We could maybe use a trie.
# Actually no need for that, just group numbers by set bit and select group with most elements

class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        groups = 24 * [0]
        for candidate in candidates:
            for i in range(24):
                groups[i] += ((1 << i) & candidate) != 0
        return max(groups)