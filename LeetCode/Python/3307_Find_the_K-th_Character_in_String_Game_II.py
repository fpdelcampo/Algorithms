# Note k is bounded by 10^14.  Each step results in doubling the size of the string
# I think binary can be used in some interesting way here
# Let's say that I want to solve for k = 14 and some random operations
# Then if I have the string after the second to last operation and its 7th char, I can figure at the answer
# If I wanted the 7th char, then I would need the 3 char of the previous one
# If I wanted the 3rd char, I would only need the 1st char at the previous step
# P(K, O) = P(K / 2, O-1) where K represents the "index" of interest and O - 1 represents the state after applying the prior operation
# This gives us a trajectory to follow.  If we have k = 9, then we look at 1, 1, 1, 1, 9
class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        binary = bin(k - 1)[2:]
        amount = 0
        for i in range(len(binary)):
            if operations[len(binary) - i - 1] == 1 and binary[i] == "1":
                amount += 1
        return chr(ord('a') + (amount % 26))