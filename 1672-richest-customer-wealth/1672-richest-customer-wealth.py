class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        reachest = 0
        for cust in accounts:

            wealth = sum(cust)
            reachest = max(wealth,reachest)
        return reachest

        