class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        count = {}

        for c in s:
            count[c] = count.get(c, 0) + 1

        for c in t:
            if c not in count or count[c] == 0:
                return c

            count[c] -= 1