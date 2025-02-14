class ProductOfNumbers:

    def __init__(self):
        self.products = [1]

    def add(self, num: int) -> None:
        if num == 0:
            self.products = [1]
        else:
            self.products.append(self.products[-1] * num)
        # print(self.products)

    def getProduct(self, k: int) -> int:
        if k + 1 > len(self.products):
            return 0
        # print(k, self.products[-1], self.products[-(k + 1)])
        return self.products[-1] // self.products[-(k + 1)]

# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)