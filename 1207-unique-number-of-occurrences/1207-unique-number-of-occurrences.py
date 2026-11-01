class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        occ = {}

        for i in arr:
            occ[i] = occ.get(i, 0) + 1

        return len(occ.values()) == len(set(occ.values()))
        