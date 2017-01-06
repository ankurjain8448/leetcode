class Solution {
public:
    vector<int> findDisappearedNumbers(vector<int>& nums) {
        vector<int> missing ;
        int n = nums.size();
        int index = 0 , m = n+1;
        for (int i = 0;i< n ; i++){
            index = (nums[i]-1) % m;
            nums[index] = nums[index] + n + 1; 
        }
        for(int i = 0; i < n; i++)
            if (nums[i] < m)
                missing.push_back(i+1);
        return missing;
    }
};