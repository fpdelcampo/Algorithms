class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = maxSize * [None]
        self.size = 0

    def push(self, x: int) -> None:
        if self.size < len(self.stack):
            self.stack[self.size] = x
            self.size += 1

    def pop(self) -> int:
        if self.size > 0:
            res = self.stack[self.size - 1]
            self.size -= 1
            return res
        else:
            return -1

    def increment(self, k: int, val: int) -> None:
        for i in range(min(k, len(self.stack))):
            if self.stack[i] == None:
                break
            self.stack[i] += val

# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)