class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        res = []
        num = "123456789"
        lo = int(ceil(log10(low)))
        hi = int(ceil(log10(high)))
        i = lo
        while i <= hi:
            for j in range(9 - i + 1):
                if low <= int(num[j:j+i]) <= high:
                    res.append(int(num[j:j+i]))
            i += 1
        return res