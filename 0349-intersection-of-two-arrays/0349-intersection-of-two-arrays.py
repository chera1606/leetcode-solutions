class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:

        interSec = set(nums1) & set(nums2)
        return list(interSec)
