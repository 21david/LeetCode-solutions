class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        mod = 10 ** 9 + 7

        # Count number of points on each horizontal line
        rows = defaultdict(int)  # num of points per horizontal line with at least 2 points
        for x, y in points:
            rows[y] += 1

        rows = dict(rows)

        # Delete rows with just 1 point
        to_delete = []
        for row in rows:
            val = rows[row]
            if val <= 1:
                to_delete.append(row)
        for to_delete_val in to_delete:
            del rows[to_delete_val]

        # Apply combinatorics equation to each row to find number of combinations of picking 2 points
        for row in rows:
            val = rows[row]
            rows[row] = val * (val - 1) // 2   # OR rows[row] = int(math.factorial(val) / (2 * math.factorial(val - 2)))  # OR math.combs(val, 2) instead?

        '''
        The values (rows.values()) represent ways to pick two points from a list of points on the same horizontal line,
        since we need two points to make a side. This is after applying the combinations formula above.
        If the values are: 1, 3, 6, 10, we want this value:
            (3 * 1) + (6 * 3 + 6 * 1) + (10 * 6 + 10 * 3 + 10 * 1)
            = (3 * 1) + 6 (3 + 1) + 10 (6 + 3 + 1)  # Pull out the common factor in each
        The parenthesis part increases by the next value each time, and then gets multiplied
        by the next next value.
        Therefore, to get this calculation in O(N), we can keep the parenthesis part in acc 
        (accumulation) multiply it by the next next number, and add to the final answer.
        '''
        ans = 0
        combs = list(rows.values())
        if len(combs) == 0:
            return 0

        acc = combs[0]
        for i in range(1, len(combs)):
            comb = combs[i]
            ans += comb * acc
            acc += comb

        return ans % mod
