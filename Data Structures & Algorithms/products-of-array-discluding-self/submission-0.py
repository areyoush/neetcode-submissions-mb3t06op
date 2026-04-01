class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products = []

        for i in range(len(nums)):
            dupelist = list(nums)
            if nums[i] in dupelist:
                dupelist.remove(nums[i])
                prod = 1
                for j in dupelist:
                    prod *= j
                products.append(prod)
        return products
        
        
        