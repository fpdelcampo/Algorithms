# A simple array based implementation of a segment tree

class SegTree():
    def __init__(self, f, arr) -> None:
        self.f = f
        self.segtree = [0 for _ in range(4(len(arr)))]
        self.build(arr)

    def build(self, arr, index, left, right):
        if left == right:
            self.segtree[index] = self.arr[index]
        else:
            middle = (left + right)//2
            self.build(arr, index*2, left, middle)
            self.build(arr, 2*index+1, middle+1, right)
            self.segtree[index] = self.f(self.segtree[2*index], self.segtree(2*index+1))
