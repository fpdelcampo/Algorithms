class Solution:
    def rotate(self, string):
        res = []
        for i in range(26):
            curr = []
            for char in string:
                curr.append(chr(((ord(char)+i-ord('a'))%26)+ord('a')))
            res.append("".join(curr))
        return res

    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        piles = {}
        for string in strings:
            comp = self.rotate(string)
            hit = False
            for cmp in comp:
                if cmp in piles:
                    hit = True
                    piles[cmp].append(string)
                    break
            if not hit:
                piles[string] = [string]
        
        res = []
        for key in piles:
            res.append(list(piles[key]))
        return res