class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = {}
        for char in s:
            if char in ['A', 'E','I','O','U','a','e','i','o','u']:
                if char not in vowels:
                    vowels[char] = 1
                else:
                    vowels[char] += 1
        q = deque()
        for v in ['A', 'E','I','O','U','a','e','i','o','u']:
            if v in vowels:
                for i in range(vowels[v]):
                    q.append(v)
        new = ""
        for char in s:
            if char in ['A', 'E','I','O','U','a','e','i','o','u']:
                next = q.popleft()
                new += next
            else:
                new += char
        return new