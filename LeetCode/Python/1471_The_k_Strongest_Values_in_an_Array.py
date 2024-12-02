class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        median = -1
        if len(arr) % 2 == 1:
            median = arr[len(arr) // 2]
        else:
            median = arr[len(arr) // 2 - 1]
        mod = [[abs(num - median), num] for num in arr]
        mod.sort(key = lambda x: (-x[0], -x[1]))
        return [mod[i][1] for i in range(k)]