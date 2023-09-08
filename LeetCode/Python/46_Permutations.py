class Solution:
    # Idea is that we start at a "partial solution", we then permute until we get a complete solution and add that to the list of solutions
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        a = len(nums)
        def permutation(curr):
            if len(curr) == a:
                result.append(curr[:]) # Note that you can't just say result.append(curr) due to the way that arrays are copied in python
            else:
                for i in nums:
                    if i not in curr:
                        curr.append(i)
                        permutation(curr)
                        curr.pop()
        permutation([])
        return result