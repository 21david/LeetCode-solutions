class Solution:
    def transformStr(self, s: str, strs: List[str]) -> List[bool]:
        # if strs[i] has too many 0s or too many 1s, reject immediately
        # sort option just boils down to "can move any 1 anywhere to its right, but not to its left" or move 0s left

        n = len(s)
        zero = s.count('0')
        one = s.count('1')

        leftmost = s.index('1') if one else n

        ans = []

        for pat in strs:
            pzero = pat.count('0')
            pone = pat.count('1')

            if pzero > zero or pone > one:
                ans.append(False)
                continue

            try:
                pleftmost = pat.index('1')
            except ValueError:
                pleftmost = n
            
            if pleftmost < leftmost:
                ans.append(False)
                continue

            # assign all extra ones to the rightmost ?s as this gives the best chance
            # AI gave me a hint for this part and below
            onediff = one - pone
            pat = list(pat)
            for i in range(len(pat)-1, -1, -1):
                if pat[i] == '?':
                    if onediff >= 1:
                        pat[i] = '1'
                        onediff -= 1
                    else:
                        pat[i] = '0'

            pat = ''.join(pat)

            sc = pc = 0  # count of 1s for both strings
            flag = True
            for i in range(len(s)):
                if s[i] == '1':
                    sc += 1
                if pat[i] == '1':
                    pc += 1

                # if our curent prefix of pattern has more 1s than the same prefix of s,
                # then that would imply having to move a 1 to the left in s, which is impossible
                if pc > sc:
                    ans.append(False)
                    flag = False
                    break

            # if no prefix in pattern has more 1s than same prefix in s, then the 1s could be rearranged in s
            if flag:
                ans.append(True)

        return ans

"""
"101"
["1?1","0?1","0?0"]
"1100"
["0011","11?1","1?1?"]
"1010"
["0011"]
"000111"
["1?????", "??1???", "???1??", "??????"]
"010101"
["100101", "01????"]
"000000"
["??????", "0???00", "000000", "000001", "?????1", "10000?"]
"0"
["0", "?", "1"]
"01"
["?0"]

"01010"
["?0?0?", "00101"]
"0101"
["?0?0", "1010", "0110", "01?0"]
"""
