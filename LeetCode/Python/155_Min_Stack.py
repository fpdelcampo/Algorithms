class MinStack:
    # Key idea is that we can compare the current part of the stack with the entire rest of it
    def __init__(self):
        self.values = []

    def push(self, val: int) -> None:
        if len(self.values) == 0:
            self.values.append([val, val])
        else:
            self.values.append([val, min(val, self.values[-1][1])])

    def pop(self) -> None:
        self.values.pop()

    def top(self) -> int:
        return self.values[-1][0]

    def getMin(self) -> int:
        return self.values[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()