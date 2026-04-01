class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        list2 = []
        for i in nums:
            list2.append(i)
        for j in nums:
            list2.append(j)

        return(list2)
        