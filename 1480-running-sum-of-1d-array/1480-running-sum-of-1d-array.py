class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        out = [nums[0]]
        for i in range(len(nums) - 1):
            j = out[i]+nums[i+1]
            out.append(j)
        return out

      

        