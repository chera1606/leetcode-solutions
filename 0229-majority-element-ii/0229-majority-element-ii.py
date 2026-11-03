class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        count = {}
        n= len(nums)
        result=[]
        for num in nums:
            if num in count:
                count[num]+=1
            else:
                count[num]=1
        for left ,right in count.items():
            if right > n/3:
                result.append(left)
        return result
        