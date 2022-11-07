class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int best = INT_MIN;
        int curr = 0;
        for(int i = 0; i<size(nums);i++) {
            curr=max(nums[i]+curr, nums[i]);
            best=max(best, curr);
        }
        return best;
    }
};