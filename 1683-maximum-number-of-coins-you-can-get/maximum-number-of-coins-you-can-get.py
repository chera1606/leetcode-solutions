class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        
        ans = 0
        left = 0
        right = len(piles) - 1
        
        while left < right:
            right -= 1          
            ans += piles[right] 
            right -= 1
            left += 1          
        
        return ans