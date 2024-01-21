class Solution:
    def findHighAccessEmployees(self, access_times: List[List[str]]) -> List[str]:
        count = {}
        for i in range(len(access_times)):
            if access_times[i][0] in count:
                count[access_times[i][0]].append(int(access_times[i][1]))
            else:
                count[access_times[i][0]] = [int(access_times[i][1])]
        res = []
        for key in count:
            count[key].sort()
        print(count)

        for key in count:
            tmp = []
            hit = False
            for i in range(1, len(count[key])):
                tmp.append(count[key][i]- count[key][i-1])
            print(key, tmp)
            for i in range(1, len(tmp)):
                if tmp[i]+tmp[i-1] < 100:
                    hit = True
                    break
            if hit and len(tmp) >= 2:
                res.append(key)
        return res