class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k){ 
        unordered_map<int, int>myMap;
        for(int num : nums){
            if(myMap.find(num) == myMap.end()){
                myMap[num] = 1;
            }else{
                myMap[num]++;
            }
        }

        vector<int> maxValues;
        
        for(int i=0; i<k; ++i){
            auto maxIt = max_element(myMap.begin(), myMap.end(), 
            [](const std::pair<int, int>& p1, const std::pair<int, int>& p2){
                
                return p1.second < p2.second;
            });
            maxValues.push_back(maxIt->first);

        
            myMap.erase(maxIt);
        }

    return maxValues;
        
    }
};
