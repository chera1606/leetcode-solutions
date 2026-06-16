class Solution:
    def sortColors(self, nums: List[int]) -> None:
        n = len(nums)

        for i in range(n):
            curr_min = i

            for j in range(i+1,n):
                if nums[j]< nums[curr_min]:
                    curr_min = j
            nums[i],nums[curr_min] = nums[curr_min],nums[i]      

        return nums    
        