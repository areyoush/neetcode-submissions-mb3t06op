class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def hours(k):
            hrs = 0
            for pile in piles:
                hrs += math.ceil(pile / k)
            return hrs
        
        left = 1
        right = max(piles)
        result = right

        while left <= right:
            mid = (left + right) // 2
        
            if hours(mid) <= h:
                result = mid
                right = mid - 1
        
            else:
                left = mid + 1
        
        return result
        

        


        