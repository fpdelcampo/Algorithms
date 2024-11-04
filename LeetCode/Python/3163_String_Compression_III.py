class Solution:
    def compressedString(self, word: str) -> str:
        if len(word) == 1:
            return "1"+word
        cnt = 1
        comp = ""
        for i in range(1, len(word)):
            if word[i] == word[i - 1]:
                if cnt == 9:
                    comp += '9'
                    comp += word[i]
                    cnt = 1
                else:
                    cnt += 1
            else:
                comp += str(cnt)
                comp += word[i - 1]
                cnt = 1
        return comp + str(cnt) + word[-1]
        