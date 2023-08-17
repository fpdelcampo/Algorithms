def hIndexMN(nums): # We want to find the largest k such that there are exactly k elements in nums that are greater than or equal to k; nums is unsorted
    h=0
    for i in reversed(nums):
        if h+1<=i:
            h+=1
    return h

def hIndexN(nums):
    ref = [0 for i in range(len(nums))]
    for i in nums:
        if i >= len(nums):
            ref[-1]+=1
        else:
            ref[i]+=1
    cumulative = [0 for i in range(len(nums))]
    cumulative[0] = ref[-1]
    for i in range(len(nums)-1):
        cumulative[i+1]=ref[i+1]+cumulative[i]
    best = 0
    print(cumulative)
    for i in range(len(nums)):
        if cumulative[i] >= i+1:
            best = i+1
    return best

if __name__ == "__main__":
    x = [2,4,5,7,8,9,30,70]
    x1 =  [2,4,7,30]
    target = 5
    target1 = 3
    print(hIndexMN(x), target)
    print(hIndexN(x), target)
    print(hIndexMN(x1), target1)
    print(hIndexN(x1), target1)