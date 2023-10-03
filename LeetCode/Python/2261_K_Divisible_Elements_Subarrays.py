class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        if len(nums)<k:
            return 0
        n = [x%p for x in nums]
        total=0
        seen=set()
        for i in range(len(n)):
            j=i
            count=0
            t=0
            x=""
            while j<len(n) and t<=k:
                if n[j]==0 and t==k:
                    print(j)
                    break
                if n[j]==0:
                    t+=1
                x+=str(nums[j])+"_"
                if x not in seen:
                    seen.add(x)
                    count+=1
                j+=1
            total+=count
        return total