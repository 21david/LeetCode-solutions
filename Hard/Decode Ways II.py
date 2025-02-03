'''
At each index, take one digit, and recursively compute the answer to the rest 
of the string. Then take two digits and do the same thing again. Each time, 
add the result of trying both things, which gives us the total number of valid 
decodings.

We may come across the same recursive subproblems, because the recursive call 
that takes two digits travels faster, and then the one that takes one digit 
eventually catches up, resulting in it reaching a problem that has already 
been solved, so memoization / DP will make this linear instead of exponential.

TC: O(N)
SC: O(N)
'''
class Solution:
    def numDecodings(self, s: str) -> int:
        S = len(s)

        @cache
        def try_all_combinations(i):
            if i == S:
                return 1

            count = 0

            # Take one digit
            one_digit = s[i:i+1]

            if one_digit == '*':
                count += try_all_combinations(i+1) * 9

            elif one_digit != '0':
                count += try_all_combinations(i+1)

            if i+2 > S:
                return count

            # Take two digits
            two_digits = s[i:i+2]

            if two_digits == '**':
                count += try_all_combinations(i+2) * 15  # 9 + 6, for 11 to 19 and 21 to 26, since * can't be 0

            elif two_digits[0] == '*':  # Example: *9
                if int(two_digits[1]) <= 6:
                    count += try_all_combinations(i+2) * 2
                else:
                    count += try_all_combinations(i+2)

            elif two_digits[-1] == '*':  # Example: 7*
                if two_digits[0] == '1': # 1 to 9 = 9
                    count += try_all_combinations(i+2) * 9
                elif two_digits[0] == '2':  # 21 to 26 = 6
                    count += try_all_combinations(i+2) * 6
                else:
                    return count

            elif 10 <= int(two_digits) <= 26:  # Example: 23
                count += try_all_combinations(i+2)

            return count % (10**9+7)

        return try_all_combinations(0)



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
Same exact solution, but memoized with a dictionary.
'''
class Solution:
    def numDecodings(self, s: str) -> int:
        S = len(s)

        memo = { S: 1 }  # Stores { idx : numDecodings for s[idx:] }
        def try_all_combinations(i):
            if i in memo:
                return memo[i]

            count = 0

            # Take one digit
            one_digit = s[i:i+1]

            if one_digit == '*':
                count += try_all_combinations(i+1) * 9

            elif one_digit != '0':
                count += try_all_combinations(i+1)

            if i+2 > S:
                return count

            # Take two digits
            two_digits = s[i:i+2]

            if two_digits == '**':
                count += try_all_combinations(i+2) * 15  # 9 + 6, for 11 to 19 and 21 to 26, since * can't be 0

            elif two_digits[0] == '*':  # Example: *9
                if int(two_digits[1]) <= 6:
                    count += try_all_combinations(i+2) * 2
                else:
                    count += try_all_combinations(i+2)

            elif two_digits[-1] == '*':  # Example: 7*
                if two_digits[0] == '1': # 1 to 9 = 9
                    count += try_all_combinations(i+2) * 9
                elif two_digits[0] == '2':  # 21 to 26 = 6
                    count += try_all_combinations(i+2) * 6
                else:
                    return count

            elif 10 <= int(two_digits) <= 26:  # Example: 23
                count += try_all_combinations(i+2)

            answer_at_i = count % (10**9+7)
            memo[i] = answer_at_i
            return answer_at_i

        return try_all_combinations(0)


