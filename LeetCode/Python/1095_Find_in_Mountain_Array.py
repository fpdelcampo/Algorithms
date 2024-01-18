# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        n = mountain_arr.length()
        l = 0
        r = n - 1
        m = (l + r) // 2
        a = -1
        b = -1
        c = -1
        index = 10001
        while l <= r:
            
            a = mountain_arr.get(m - 1)
            b = mountain_arr.get(m)
            c = mountain_arr.get(m + 1)
            if target == a:
                index = min(index, m - 1)
            if target == b:
                index = min(index, m)
            if target == c:
                index = min(index, m + 1)
            if a < b > c:
                break
            elif a < b < c:
                l = m + 1
            else:
                r = m
            m = (l + r) // 2
        if target == b:
            return m
        l1 = 0 
        r1 = m - 1
        l2 = m + 1
        r2 = n - 1
        while l1 <= r1:
            m1 = (l1 + r1) // 2
            x = mountain_arr.get(m1)
            if x == target:
                return min(index, m1)
            elif x < target:
                l1 = m1 + 1
            else:
                r1 = m1 - 1
            m = (l + r) // 2

        while l2 <= r2:     
            m2 = (l2 + r2) // 2
            x = mountain_arr.get(m2)
            if x == target:
                return min(index, m2)
            elif x > target:
                l2 = m2 + 1
            else:
                r2 = m2 - 1        
        return -1