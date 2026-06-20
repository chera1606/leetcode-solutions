class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()

        n = len(piles) // 3
        ans = 0
        idx = len(piles) - 2

        for _ in range(n):
            ans += piles[idx]
            idx -= 2

        return ans