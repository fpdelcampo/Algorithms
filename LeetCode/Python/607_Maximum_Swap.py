class Solution:
    # Idea: take the largest digit that isn't in the "right" place and swap it there
    # If we have 9999937, then the 7 isn't in the right place, so we want to get 9999973
    # 9995324 --> 9995432
    # So we find the smallest i such that num[i] < num[j] for some j
    def maximumSwap(self, num: int) -> int:
        digits = [int(digit) for digit in str(num)]
        desc = 9
        largest = -1
        idx = -1
        for i in range(len(digits)):
            if digits[i] > desc:
                if digits[i] >= largest:
                    idx = i
                    largest = digits[i]
            desc = min(desc, digits[i])
        if largest == -1:
            return num
        for i in range(len(digits)):
            if digits[i] < largest:
                digits[i], digits[idx] = digits[idx], digits[i]
                break
        return int("".join([str(x) for x in digits]))
            