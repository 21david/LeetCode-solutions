class Solution:
    def numDecodings(self, s: str) -> int:
        S = len(s)

        @cache
        def decode(i):
            # Base case
            if i == S:
                return 1

            count = 0

            # Take one digit
            one_digit = s[i:i+1]

            if one_digit == '*':
                count += decode(i+1) * 9

            elif one_digit != '0':
                count += decode(i+1)

            if i+2 > S:
                return count

            # Take two digits
            two_digits = s[i:i+2]

            if two_digits == '**':
                count += decode(i+2) * 15  # 9 + 6, for 11 to 19 and 21 to 26, since * can't be 0

            elif two_digits[0] == '*':  # Example: *9
                if int(two_digits[1]) <= 6:
                    count += decode(i+2) * 2
                else:
                    count += decode(i+2)

            elif two_digits[-1] == '*':  # Example: 7*
                if two_digits[0] == '1': # 1 to 9 = 9
                    count += decode(i+2) * 9
                elif two_digits[0] == '2':  # 21 to 26 = 6
                    count += decode(i+2) * 6
                else:
                    return count

            elif 10 <= int(two_digits) <= 26:  # Example: 23
                count += decode(i+2)

            return count % (10**9+7)

        return decode(0)



'''
Test cases:
"*"
"1*"
"2*"
"**"
"*1"
"*3"
"*9"
"*********"
'''



'''
Same solution, but memoized with a dictionary.
'''
class Solution:
    def numDecodings(self, s: str) -> int:
        S = len(s)

        memo = { S: 1 }  # Stores { idx : numDecodings for s[idx:] }
        def decode(i):
            if i in memo:
                return memo[i]

            count = 0

            # Take one digit
            one_digit = s[i:i+1]

            if one_digit == '*':
                count += decode(i+1) * 9

            elif one_digit != '0':
                count += decode(i+1)

            if i+2 > S:
                return count

            # Take two digits
            two_digits = s[i:i+2]

            if two_digits == '**':
                count += decode(i+2) * 15  # 9 + 6, for 11 to 19 and 21 to 26, since * can't be 0

            elif two_digits[0] == '*':  # Example: *9
                if int(two_digits[1]) <= 6:
                    count += decode(i+2) * 2
                else:
                    count += decode(i+2)

            elif two_digits[-1] == '*':  # Example: 7*
                if two_digits[0] == '1': # 1 to 9 = 9
                    count += decode(i+2) * 9
                elif two_digits[0] == '2':  # 21 to 26 = 6
                    count += decode(i+2) * 6
                else:
                    return count

            elif 10 <= int(two_digits) <= 26:  # Example: 23
                count += decode(i+2)

            answer_at_i = count % (10**9+7)
            memo[i] = answer_at_i
            return answer_at_i

        return decode(0)

