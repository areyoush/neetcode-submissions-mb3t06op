class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> myMap;
        for(int i=0; i<nums.size(); i++){
            int num = nums[i];
            int more = target - num;
            if(myMap.find(more) != myMap.end()){
                return {myMap.at(more), i};
            }
            myMap[num] = i;
        }
        return {-1, -1};
        
    }
};
