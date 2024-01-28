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
    print(segtree.segtree)
    successes = 0
    for _ in range(500):
        left = random.randint(0, 999)
        right = random.randint(left, 999)
        if segtree.query(left, right)  == (right * (right + 1)) // 2 - (left * (left - 1)) // 2:
            print(left, right)
            successes += 1
    print(segtree.query(500, 717))
    print(f"Successes: {successes}; Total: {500}")

if __name__ == "__main__":
    main()
# import random
# arr = list(range(1000))
# tree = [0] * 4 * len(arr)
# def build(v, tl, tr):
#     if tl == tr:
#         tree[v] = arr[tl]
#     else:
#         tm = (tl + tr) // 2
#         build(2 * v, tl, tm)
#         build(2 * v + 1, tm + 1, tr)
#         tree[v] = tree[2 * v] + tree[2 * v + 1]
# def query_util(v, tl, tr, l, r):
#     if l > r:
#         return 0
#     if l == tl and r == tr:
#         return tree[v]
#     tm = (tl + tr) // 2
#     return query_util(2 * v, tl, tm, l, min(r, tm)) + query_util(2 * v + 1, tm + 1, tr, max(l, tm + 1), r)
# def query(l, r):
#     return query_util(1, 0, len(arr) - 1, l, r)

# build(1, 0, len(arr) - 1)
# res = query(3, 500)
# success = 0
# for i in range(500):
#     left = random.randint(0, 999)
#     right = random.randint(left, 999)
#     if query(left, right) != (right * (right + 1)) // 2 - (left * (left - 1)) // 2:
#         print(left, right)
#     else:
#         success += 1
# print(success)