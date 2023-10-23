class ValidWordAbbr:

    def __init__(self, dictionary: List[str]):
        self.dictionary = {}
        for word in dictionary:
            middle = str(len(word)-2) if len(word) > 2 else ""
            encode = word[0] + middle + word[-1]
            if encode in self.dictionary:
                self.dictionary[encode].add(word)
            else:
                self.dictionary[encode] = set([word])

    def isUnique(self, word: str) -> bool:
        middle = str(len(word)-2) if len(word) > 2 else ""
        encode = word[0] + middle + word[-1]
        if encode not in self.dictionary or (encode in self.dictionary and self.dictionary[encode] == set([word])):
            return True
        return False

# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)