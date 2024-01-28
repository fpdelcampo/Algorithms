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
    
    def update(self, index, value):
        pass

    def query_helper(self, v, tl, tr, l , r):
        if tl > tr:
            return self.identity
        
        if l == tl and r == tr:
            return self.segtree[v]
        
        tm = (tl + tr) // 2
        print(tl, tm, tr, l, r)
        return self.f(self.query_helper(2 * v, tl, tm, l, min(r, tm)), self.query_helper(2 * v + 1, tm + 1, tr, max(l, tm + 1), r))
    
    def query(self, l, r):
        return self.query_helper(1, 0, len(self.arr) - 1, l, r)

def main():
    arr = list(range(8))
    segtree = Segtree(arr)
    print(segtree.segtree)
    print(segtree.f(1, 2))
    result = segtree.query(0, 5)
    print(result)

if __name__ == "__main__":
    main()