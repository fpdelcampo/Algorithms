class Solution:
    # Want to use a somewhat greedy approach
    
    def decodeAtIndex(self, s: str, k: int) -> str:
        
        curr = 0
        for i in s:
            if i.isnumeric():
                curr *= int(i)
            else:
                curr += 1
        for i in s[::-1]:
            k %= curr
            print(i, i.isnumeric())
            if k == 0 and not i.isnumeric():
                return i
            if i.isnumeric():
                curr /= int(i)
            else:
                curr -= 1