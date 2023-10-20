class Solution:
    def countAndSay(self, n: int) -> str:
        sequence = "1"
        if n == 1:
            return sequence
        for i in range(n-1):
            # We want to generate the appropriate string given the last entry in the sequence
            last = sequence[0]
            streak = 0
            char = []
            freq = []
            for j in sequence:
                if j == last:
                    streak += 1
                else:
                    char.append(last)
                    freq.append(streak)
                    last = j
                    streak = 1

            char.append(last)
            freq.append(streak)
            s = ""
            for k in range(len(char)):
                s += str(freq[k])
                s += char[k]
            sequence = s
        return sequence