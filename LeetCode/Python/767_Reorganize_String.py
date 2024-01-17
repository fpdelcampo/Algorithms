class Solution:
    def reorganizeString(self, s: str) -> str:
        if len(s) == 1:
            return s
        c = Counter(s)
        res = ""
        while len(res) < len(s):
            if len(c) == 1: 
                a, b = c.most_common()[0]
                if res and res[-1] == a:
                    return ""
                else:
                    res += a
            else:
                tmp = c.most_common(2)
                first = tmp[0]
                second = tmp[1]
                x, _ = first
                y, _ = second
                if res and res[-1] == x:
                    res += y
                    if c[y] == 1:
                        del c[y]
                    else:
                        c[y] -= 1
                else:
                    res += x
                    if c[x] == 1:
                        del c[x]
                    else:
                        c[x] -= 1
        return res