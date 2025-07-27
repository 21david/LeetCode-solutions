# TC = O(C)
# SC = O(C)
class Solution:
    def numOfSubsequences(self, s: str) -> int:
        # Remove any distracting characters
        s = [c for c in s if c in ('L','T','C')]
        s = ''.join(s)
        S = len(s)
        
        lct = [0] * 3

        for c in s:
            match c:
                case 'L':
                    lct[0] += 1
                case 'C':
                    lct[1] += 1
                case 'T':
                    lct[2] += 1
                    
        letters_present = sum(bool(count) for count in lct)
        
        if letters_present <= 1:
            # Missing at least 2 letters, impossible to get an LCT
            return 0
            
        elif letters_present == 3:
            # Answer is either adding an L to the start, T to the end, or C somewhere in the middle
            add_l = self.calc_combs('L' + s)
            add_t = self.calc_combs(s + 'T')
            add_c = self.add_best_c(s)
            return max(add_l, add_t, add_c)
                        
        elif (letters_present == 2 and lct[0] == 0):
             # Missing an L, just add to the beginning and calculate
            return self.calc_combs('L' + s)
            
        elif (letters_present == 2 and lct[2] == 0):
            # Missing a T, just add to the end and calculate
            return self.calc_combs(s + 'T')
            
        elif letters_present == 2 and lct[1] == 0:
            # Missing a C - find the best spot for C
            return self.add_best_c(s)
            
    def add_best_c(self, s):
        S = len(s)
        ls = [0] * S
        ts = [0] * S

        # prefix sum of Ls going from left to right
        l = 0
        for i in range(S):
            if s[i] == 'L':
                l += 1
            ls[i] = l

        # prefix sum of Ts going from right to left
        t = 0
        for i in range(S-1, -1, -1):
            if s[i] == 'T':
                t += 1
            ts[i] = t

        # Find max product of Ls and Ts at any index - this is max number of LT combinations you can get from putting a C in between
        max_combs = 0
        idx = 0
        for i in range(S):
            res = ls[i] * ts[i]
            if res > max_combs:
                max_combs = res
                idx = i
                
        # Put a C in that spot and compute the new answer
        return self.calc_combs(s[:idx+1] + 'C' + s[idx+1:])

    def calc_combs(self, s):
        S = len(s)
        ans = t = 0
        readycs = 0  # number of available C->T combinations at any moment
        for i in range(S-1, -1, -1):
            match s[i]:
                case 'L':
                    # There are 'readycs' available combinations of C->T for the current L
                    ans += readycs
                case 'C':
                    # This current C has access to 't' Ts, so add these combinations to 'readycs'
                    readycs += t
                case 'T':
                    t += 1
        return ans
