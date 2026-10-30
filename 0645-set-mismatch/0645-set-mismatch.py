class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        unique = set(nums)
        dub = sum(nums)-sum(unique)

        n = len(nums)
        for i in range(1, n + 1):
            if i not in unique:
                lost = i
                break 
                
        return [dub, lost]