class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        a = 0
        b = 0
        if len(colors) <= 2:
            return False
        for idx in range(1,len(colors)-1):
            if colors[idx-1] == colors[idx] and colors[idx] == colors[idx+1]:
                if colors[idx] == 'A':
                    a += 1
                else:
                    b += 1 
        if a > b:
            return True
        else:
            return False