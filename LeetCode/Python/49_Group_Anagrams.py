class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lookup = {}
        for word in strs:
            abbr = self.abbreviate(word)
            if abbr not in lookup:
                lookup[abbr] = [word]
            else:
                lookup[abbr].append(word)
        res = []
        for key in lookup:
            res.append(lookup[key])
        return res
    
    def abbreviate(self, word):
        init = 26*[0]
        for char in word:
            init[ord(char)-ord('a')] += 1
        return tuple(init)