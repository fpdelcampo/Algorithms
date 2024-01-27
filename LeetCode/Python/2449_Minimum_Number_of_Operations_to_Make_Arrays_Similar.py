class Solution:
    # Can easily make this O(1) space if I, without loss of generality, negate either the evens or the odds.
    def makeSimilar(self, nums: List[int], target: List[int]) -> int:
        o1 = []
        e1 = []
        o2 = []
        e2 = []
        for i in range(len(nums)):
            if nums[i] % 2:
                o1.append(nums[i])
            else:
                e1.append(nums[i])
            if target[i] % 2:
                o2.append(target[i])
            else:
                e2.append(target[i])
        o1.sort()
        e1.sort()
        o2.sort()
        e2.sort()
        r1 = 0
        r2 = 0
        for i in range(len(o1)):
            if o1[i] > o2[i]:
                r1 += (o1[i] - o2[i]) // 2
            else: 
                r2 += (o2[i] - o1[i]) // 2
        r3 = 0
        r4 = 0
        for i in range(len(e1)):
            if e1[i] > e2[i]:
                r3 += (e1[i] - e2[i]) // 2
            else:
                r4 += (e2[i] - e1[i]) // 2
        if r1 + r2 == r3 + r4:
            return r1 + r2
        else:
            return r1 + r3
