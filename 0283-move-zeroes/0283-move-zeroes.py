class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        n = len(nums)
        ptr = 0

        for i in range(n):
            if nums[i] != 0:
                nums[ptr] = nums[i]
                ptr += 1

        while ptr < n:
            nums[ptr] = 0
            ptr += 1
            
        
        