class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sor_nums = sorted(nums)
        n = len(nums)

        counts = {}

        for i in range(n):
            if sor_nums[i] not in counts:
                counts[sor_nums[i]] = i

        result = []

        for num in nums:
            result.append(counts[num])

        return result