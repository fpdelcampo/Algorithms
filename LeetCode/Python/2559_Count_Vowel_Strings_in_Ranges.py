class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        arr = [1 if words[i][0] in vowels and words[i][-1] in vowels else 0 for i in range(len(words))]
        pref = [0]
        for i in range(len(words)):
            pref.append(pref[i] + arr[i])
        res = []
        for query in queries:
            left, right = query
            res.append(pref[right + 1] - pref[left])
        return res
