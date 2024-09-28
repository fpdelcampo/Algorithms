# Idea is to store prefix array such that prefix[i] = arr[0] ^ arr[1] ... arr[i].
# Then if we want arr[left] ^ arr[left + 1] ^ ... arr[right], we can take prefix[right] ^ prefix[left - 1], since XOR is associative and its own inverse

class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prefix = [0]
        for i in range(len(arr)):
            prefix.append(arr[i] ^ prefix[-1])
        res = []
        for query in queries:
            left, right = query
            res.append(prefix[right + 1] ^ prefix[left])
        return res