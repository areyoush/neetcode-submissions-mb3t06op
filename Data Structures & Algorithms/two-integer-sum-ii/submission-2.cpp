class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {

        int leftpointer = 0;
        int rightpointer = numbers.size()-1;

        while(leftpointer < rightpointer){
            if (numbers[leftpointer] + numbers[rightpointer] == target){
                return {leftpointer+1, rightpointer+1};
            }
            else if (numbers[leftpointer] + numbers[rightpointer] < target){
                leftpointer++;
            }
            else{
                --rightpointer;
            }

        }
        
        
    }
};
