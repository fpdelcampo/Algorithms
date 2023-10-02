class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int l = 0;
        int r = numbers.size()-1;
        vector<int> solution;
        while(true) {
            if(numbers[l]+numbers[r]==target) {
                solution.push_back(l+1);
                solution.push_back(r+1);
                return solution;
            }
            if(numbers[l]+numbers[r]>target) {
                r--;
            }
            if(numbers[l]+numbers[r]<target) {
                l++;
            }
        }
    }
};