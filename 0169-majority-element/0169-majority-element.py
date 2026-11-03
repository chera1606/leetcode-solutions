class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        count = {}
        n= len(nums)
        for num in nums:
            if num in count:
                count[num]+=1
            else:
                count[num]=1
        for left ,right in count.items():
            if right > n/2:
                return left