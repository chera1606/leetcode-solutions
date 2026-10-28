class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        nod = len(set(nums))
        cl = len(nums)

        if nod == cl:
            return False
        return True
        