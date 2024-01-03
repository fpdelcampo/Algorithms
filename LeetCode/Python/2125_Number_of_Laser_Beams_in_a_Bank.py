class Solution:
    # Pseudocode -> count ones in each row and multiply with full row before and after
    def numberOfBeams(self, bank: List[str]) -> int:
        prev = 0
        count = 0
        for x in bank:
            cnt = x.count('1')
            if cnt != 0:
                count += prev*cnt
                prev = cnt
        return count