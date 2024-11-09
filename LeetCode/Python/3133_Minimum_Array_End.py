# Basically, take the unset bits in x.  Some of these will be set.  Get the binary representation of n.  From left to right, if the ith bit in n is set, set the ith unset bit in x.

class Solution:
    def minEnd(self, n: int, x: int) -> int:
        unset_bits = []
        for i in range(64):
            if (1 << i) & x == 0:
                unset_bits.append(i)

        binary = bin(n - 1)[2:][::-1]
        i = 0
        for bit in binary:
            if bit == '1':
                x |= (1 << unset_bits[i])
            i += 1
        return x