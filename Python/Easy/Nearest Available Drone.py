class Solution:
    def nearestDrone(self, drones: list[list[int]], target: list[int]) -> int:
        tx, ty = target
        i = 0
        ans = math.inf
        md = mdi = 0
        for x, y, r in drones:
            md = abs(tx - x) + abs(ty - y)
            if md <= r and md < ans:
                ans = md
                mdi = i
            i += 1

        return mdi if ans != math.inf else -1
