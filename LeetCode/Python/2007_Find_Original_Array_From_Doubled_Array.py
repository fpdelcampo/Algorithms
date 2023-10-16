class Solution:
    # If we sort the array, then we know that the smallest element must belong to nums
    # We can then filter out multiples and repeat
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        changed.sort()
        c = Counter(changed)
        ans = []
        if len(changed) % 2 != 0 or (0 in c and c[0] % 2 != 0):
            return []
        for i in range(len(changed)):
            if changed[i] != 0 and c[changed[i]] > 0 and 2*changed[i] in c and c[2*changed[i]] > 0:
                ans.append(changed[i])
                c[changed[i]] -= 1
                c[2*changed[i]] -= 1
        if 0 in c:
            for i in range(c[0]//2):
                ans.append(0)        
        return ans if 2*len(ans) == len(changed) else []
