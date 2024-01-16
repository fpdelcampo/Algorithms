class RandomizedSet:

    def __init__(self):
        self.data = {}
        self.index = []

    def insert(self, val: int) -> bool:
        res = not val in self.data
        if not res:
            return res
        self.data[val] = len(self.index)
        self.index.append(val)
        return res

    def remove(self, val: int) -> bool:
        res = val in self.data
        if not res:
            return res
        last, idx = self.index[-1], self.data[val]
        self.index[idx] = last
        self.data[last] = idx
        del self.data[val]
        self.index.pop()
        return res

    def getRandom(self) -> int:
        return random.choice(self.index)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()