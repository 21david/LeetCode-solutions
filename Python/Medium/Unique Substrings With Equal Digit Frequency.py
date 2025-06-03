class Solution:
    def equalDigitFrequency(self, s: str) -> int:
        # Create counts matrix (prefix sum for each digit)
        N = len(s)
        counts = [[0] * (N + 1) for _ in range(10)]
        for i in range(N):
            # Copy previous columns values to current column
            for digit in range(10):
                counts[digit][i+1] = counts[digit][i]

            curr_digit = ord(s[i]) - ord('0')
            counts[curr_digit][i+1] += 1

        # print(str(counts).replace('], ', '],\n '))  # See the matrix

        # Go through each possible substring, use the matrix to check 
        # if each one is a valid substring in O(1) time
        answer = 0
        seen_substrs = set()
        for i in range(N):
            curr_substr = []
            for j in range(i+1, N+1):
                curr_substr.append(s[j-1])

                # Subtract column j from i to get the counts of the current substring. O(1)
                curr_counts = [0] * 10
                for digit in range(10):
                    curr_counts[digit] = counts[digit][j] - counts[digit][i]

                # Check if all counts in curr_counts are the same. O(1)
                all_same = True
                base = -1
                for count in curr_counts:
                    if base == -1 and count:
                        base = count
                    elif base != -1 and count and count != base:
                        all_same = False
                        break

                if all_same:
                    seen_substrs.add(''.join(curr_substr))

        # print(str(seen_substrs).replace("', ", "',\n "))  # See the substrings
        
        return len(seen_substrs)
