class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        rows = []
        for row in box:
            last = deque([])
            new = ['' for i in range(len(row))]
            for i in range(len(row) -1, -1, -1):
                if row[i] == '#':
                    if last:
                        idx = last.popleft()
                        new[idx] = '#'
                        new[i] = '.'
                        last.append(i)
                    else:
                        new[i] = row[i]
                elif row[i] == '.':
                    last.append(i)
                    new[i] = row[i]
                else:
                    last = deque([])
                    new[i] = row[i]
            rows.append(new)
        # ith row corresponds to n - ith column, jth column corresponds to jth row
        res = [['' for _ in range(len(box))] for _ in range(len(box[0]))]
        for i in range(len(box)):
            for j in range(len(box[0])):
                res[j][len(box) - i - 1] = rows[i][j]
        return res