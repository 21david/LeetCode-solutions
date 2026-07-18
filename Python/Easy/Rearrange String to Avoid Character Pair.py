class Solution:
    def rearrangeString(self, s: str, x: str, y: str) -> str:
        # Modified counting sort, TC = O(len(s)), Aux SC = O(len(s))

        # Fill in count array
        abc = [0] * 26
        for c in s:
            abc[ord(c) - 97] += 1

        # Construct the answer. Start with all the ys, then all the xs
        ans = []
        ans.append(y * abc[ord(y) -97])
        ans.append(x * abc[ord(x) - 97])
        for idx, count in enumerate(abc):
            if chr((idx + 97)) in (x,y):
                continue
            ans.append(chr((idx + 97)) * count)

        # Convert answer array to string
        return ''.join(ans)
