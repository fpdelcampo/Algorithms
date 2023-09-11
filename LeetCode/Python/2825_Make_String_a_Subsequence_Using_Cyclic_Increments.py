class Solution:
    # a = 97
    # z = 122
    # Use modular arithmetic to convert the strings
    # Go through str1
    # Try to make a subsequence as you go across the array and store the longest subsequence
    
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        l = [i for i in ascii_lowercase]
        d = {}
        for i in range(len(l)):
            d[l[i]] = i

        x = 0

        for s in str1:
            if d[str2[x]] in [d[s], (d[s]+1)%26]:
                x+=1
            if x == len(str2):
                return True
        return False
