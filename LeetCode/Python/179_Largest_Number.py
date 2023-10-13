class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def compare(a, b):
            if a+b > b+a:
                return -1
            elif a+b == b+a:
                return 0
            else:
                return 1
        s = [str(x) for x in nums]
        s.sort(key=functools.cmp_to_key(compare))
        return str(int("".join(s)))