class Solution:
    def reverseWords(self, s: str) -> str:
        words = []
        curr = ""
        for char in s:
            if char == " ":
                if curr:
                    words.append(curr)
                    curr = ""
            else:
                curr += char
        if curr:
            words.append(curr)
        return " ".join(words[::-1]).strip()