import random
class Segtree():
    def __init__(self, arr, f = lambda x, y: x + y, identity = 0) -> None:
        self.arr = arr
        self.f = f
        self.identity = identity
        self.segtree = [identity for _ in range(4 * len(arr))]
        self.build(1, 0, len(arr) - 1)
    
    def build(self, v, tl, tr):
        if tl == tr:
            self.segtree[v] = self.arr[tl]
        else:
            tm = (tl + tr) // 2
            self.build(2 * v, tl, tm)
            self.build(2 * v + 1, tm + 1, tr)
            self.segtree[v] = self.f(self.segtree[2 * v], self.segtree[2 * v + 1])

    def update_helper(self, v, tl, tr, index, value):
        if tl == tr == index:
            self.segtree[v] = value
        else:
            tm = (tl + tr) // 2
            if index <= tm:
                self.update_helper(2 * v, tl, tm, index, value)
            else:
                self.update_helper(2 * v + 1, tm + 1, tr, index, value)
            self.segtree[v] = self.f(self.segtree[2 * v], self.segtree[2 * v + 1])
    
    def update(self, index, value):
        self.update_helper(1, 0, len(self.arr) - 1 , index, value)

    def query_helper(self, v, tl, tr, l , r):
        if l > r:
            return self.identity
        
        if l == tl and r == tr:
            return self.segtree[v]
        
        tm = (tl + tr) // 2
        return self.f(self.query_helper(2 * v, tl, tm, l, min(tm, r)), self.query_helper(2 * v + 1, tm + 1, tr, max(tm + 1, l), r))
    
    def query(self, l, r):
        return self.query_helper(1, 0, len(self.arr) - 1, l, r)

def main():
    arr = list(range(1000))
    segtree = Segtree(arr)
    successes = 0
    for _ in range(500):
        left = random.randint(0, 999)
        right = random.randint(left, 999)
        if segtree.query(left, right)  == (right * (right + 1)) // 2 - (left * (left - 1)) // 2:
            successes += 1
    print(f"Successes: {successes}; Total: {500}")

if __name__ == "__main__":
    main()