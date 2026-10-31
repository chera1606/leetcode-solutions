class Solution:
    def findWinners(self, matches: list[list[int]]) -> list[list[int]]:
        losses = {}

        for winner, loser in matches:
            losses.setdefault(winner, 0)
            losses[loser] = losses.get(loser, 0) + 1

        ans1 = []
        ans2 = []

        for player, count in losses.items():
            if count == 0:
                ans1.append(player)
            elif count == 1:
                ans2.append(player)

        return [sorted(ans1), sorted(ans2)]


        