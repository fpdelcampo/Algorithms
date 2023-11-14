class Solution:
    # Iterate up to sqrt(n) and look for factors
    # Then add the correspondent factor
    # If k is larger than factors, we have to return -1
    # Else, we return the kth factor
    def kthFactor(self, n: int, k: int) -> int:
        upper = (int)(n**0.5)
        factors = [1]
        for i in range(2,upper+1):
            if n%i == 0:
                factors.append(i)
        for i in range(len(factors)-1,-1,-1):
            if factors[-1] != int(n/factors[i]):
                factors.append(int(n/factors[i]))
        if k > len(factors):
            return -1
        else:
            return factors[k-1]