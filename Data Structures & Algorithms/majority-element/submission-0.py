class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums)//2]

        #if an element appears more than half the time in a array
        #then after sortng it must sit at the middle of the array

                