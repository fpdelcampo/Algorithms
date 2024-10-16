# This probably has a nice greedy solution
# Something like "if there's a lot of one letter, make as many groups of two for it as you can"
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        abc = []
        if a:
            abc.append([-a, 'a'])
        if b:
            abc.append([-b, 'b'])
        if c:
            abc.append([-c, 'c'])
        heapq.heapify(abc)
        res = ""
        last = 0
        while abc:
            qnt, char = heapq.heappop(abc)
            if len(res) >= 2 and res[-2:] == 2 * char:
                if abc:
                    tmp_qnt, tmp_char = heapq.heappop(abc)
                    res += tmp_char
                    if tmp_qnt + 1 < 0:
                        heapq.heappush(abc, [tmp_qnt + 1, tmp_char])
                    heapq.heappush(abc, [qnt, char])
                else:
                    return res
            else:
                res += min(-qnt, 2) * char
                if qnt + min(-qnt, 2):
                    heapq.heappush(abc, [qnt + min(-qnt, 2), char])
        return res