# TC = O(N + Q)
# Aux SC = O(N)
# Output SC = O(Q)
class Solution:
    def shortestDistanceColor(self, colors: List[int], queries: List[List[int]]) -> List[int]:
        C = len(colors)

        def min_dist_arr(num):
            ans = [math.inf] * C
            dist = math.inf
            for i in range(C):
                if colors[i] == num:
                    dist = 0
                else:
                    dist += 1
                ans[i] = dist

            dist = math.inf
            for i in range(C-1, -1, -1):
                if colors[i] == num:
                    dist = 0
                else:
                    dist += 1
                ans[i] = min(ans[i], dist)
            
            return [(dist if dist != math.inf else -1) for dist in ans]

        three = min_dist_arr(3)
        two = min_dist_arr(2)
        one = min_dist_arr(1)
        # print(one, two, three)

        ans = []
        for idx, num in queries:
            match num:
                case 1:
                    ans.append(one[idx])
                case 2:
                    ans.append(two[idx])
                case 3:
                    ans.append(three[idx])
        
        return ans
