class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        occ = {}

        for i in arr:
            occ[i] = occ.get(i,0)+1
            un = list(occ.values())
            unS = list(set(un))
        if len(un) == len(unS):
            return True
        return False
        