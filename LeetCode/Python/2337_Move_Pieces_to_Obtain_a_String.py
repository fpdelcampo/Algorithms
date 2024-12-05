class Solution:
    def canChange(self, start: str, target: str) -> bool:
        if ''.join(start.split('_')) != ''.join(target.split('_')):
            return False
        else:
            ls_start = []
            rs_start = []
            ls_target = []
            rs_target = []
            for i in range(len(start)):
                if start[i] == "L":
                    ls_start.append(i)
                elif start[i] == 'R':
                    rs_start.append(i)
                if target[i] == "L":
                    ls_target.append(i)
                elif target[i] == 'R':
                    rs_target.append(i)
            for i in range(len(ls_start)):
                if ls_start[i] < ls_target[i]:
                    print('a', i)
                    return False
            for i in range(len(rs_start)):
                if rs_start[i] > rs_target[i]:
                    print('b', i)
                    return False
            return True