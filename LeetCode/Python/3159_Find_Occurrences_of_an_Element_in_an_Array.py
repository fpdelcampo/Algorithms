class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        occ = []
        res = []
        for i in range(len(nums)):
            if nums[i] == x:
                occ.append(i)
        for query in queries:
            if query - 1 < len(occ):
                res.append(occ[query - 1]) 
            else:
                res.append(-1)
        return res
