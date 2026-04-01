class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_set<int> dupe;
        for(int i = 0; i<nums.size(); i++){
            if(dupe.count(nums[i]) == 0){
                dupe.insert(nums[i]);
            }
            else{
                return true;
            }
            

        }
        return false;
        
        

    }
};
