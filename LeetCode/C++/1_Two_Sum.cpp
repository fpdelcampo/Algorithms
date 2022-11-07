class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> diffmap;
        vector<int> solution;
        for(int i=0;i<nums.size();i++) {
            diffmap[target-nums[i]] = i;
        }
        for(int j=0;j<nums.size();j++) {
            if(diffmap.find(nums[j])!=diffmap.end()) {
                 if(diffmap[nums[j]]!=j) {
                    solution.push_back(j);
                    solution.push_back(diffmap[nums[j]]);
                    return solution;
                 }
            }
        }
        return solution;
    }
};