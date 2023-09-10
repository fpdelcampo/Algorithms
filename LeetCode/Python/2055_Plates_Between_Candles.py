class Solution:
    # Approach is simple:
    # Get the index of the left- and right- most pipe in the target interval
    # Call the index of the former x and the index of the latter y
    # Take y-x, then subtract 1 to get the answer
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        left_idx = []
        right_idx = []
        last_left = -1
        last_right = len(s)
        for i in range(len(s)):
            if s[i] == "|":
                last_left = i
            left_idx.append(last_left)
        
        for j in range(len(s)-1,-1,-1):
            if s[j] == "|":
                last_right = j
            right_idx.append(last_right)
        right_idx = right_idx[::-1]

        pipes = 0
        prefix_pipes = []

        for k in range(len(s)):
            if s[k] == "|":
                pipes += 1
            prefix_pipes.append(pipes)
        answers = []
        for q in queries:
            start, end = q
            l = right_idx[start]
            r = left_idx[end]
            if l == -1 or r == len(s) or l>=r:
                answers.append(0)
            else:
                answers.append(r-l - (prefix_pipes[r]-prefix_pipes[l]))
        return answers