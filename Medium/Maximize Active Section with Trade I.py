class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        S = len(s)

        # Collapse into an array of integers representing consecutive 1s and 0s
        col = []  # count of consecutive nums
        type = [] # type of consecutive nums
        
        ct = 1
        cur = s[0]
        for i in range(1, S):
            if s[i] == cur:
                ct += 1
            else:
                col.append(ct)
                type.append(cur)
                ct = 1
                cur = s[i]
        col.append(ct)
        type.append(cur)
      

        # Prefix sum arrays to quickly get total number of active sections (1s) at any index
        T = len(type)
        pf = []  # prefix_sum
        acc = 0
        for i in range(T):
            if type[i] == '0':
                pf.append(0)
            else:
                acc += col[i]
                pf.append(acc)
        pfb = []  # prefix_sum_backwards
        acc = 0
        for i in range(T - 1, -1, -1):
            if type[i] == '0':
                pfb.append(0)
            else:
                acc += col[i]
                pfb.append(acc)
        pfb.reverse()

      
        # Find max by checking how many active sections we can have by doing the flips
        # on each 1 that is surrounded by 0s
        tr_idx = -math.inf  # idx to do the trade on
        max_poss = -math.inf
        for i in range(1, T - 1):
            if (type[i-1] == type[i+1] == '0') and type[i] == '1':
                cand = col[i-1] + col[i] + col[i+1]
                if i-2 >= 0:
                    cand += pf[i-2]
                if i + 2 < T:
                    cand += pfb[i+2]

                # Update max and index of max if we found a new max
                if cand > max_poss:
                    max_poss = cand
                    tr_idx = i

        # if a trade was possible, answer is in max_poss
        if max_poss != -math.inf:
            return max_poss

        # Otherwise, count all active sections as the final answer
        return sum(num for i, num in enumerate(col) if type[i] == '1')



"""
Test cases:
"01"
"0100"
"1000100"
"01010"
"0"
"1"
"010101100"
"001101010"

"0000"
"1111"
"00100"
"101"
"""
