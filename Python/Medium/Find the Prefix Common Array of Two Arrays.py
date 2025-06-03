'''
Linear approach:
Store numbers that have been seen 1 time in one set.
When a number has been seen twice, store it in the second set.

After each iteration, the second set stores all the numbers that have 
appeared in both arrays A and B. The length of this set gives the current
value of C[i].

TC: O(N)
SC: O(N)
N = len(A) = len(B)
'''
class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        set_one = set()  # Store numbers with a count of 1
        set_two = set()  # Store numbers with a count of 2
        answer = []

        for a, b in zip(A, B):
            if a in set_one:
                set_two.add(a)
            else:
                set_one.add(a)

            if b in set_one:
                set_two.add(b)
            else:
                set_one.add(b)
            
            answer.append(len(set_two))

        return answer


'''
Using bits to keep track of seen numbers, we can make the space complexity O(1).

TC: O(N)
SC: O(1)
N = len(A) = len(B)
'''
class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        bit_set_1 = 0  # Store numbers with a count of 1
        bit_set_2 = 0  # Store numbers with a count of 2
        bit_set_1_len = bit_set_2_len = 0
        answer = []

        for a, b in zip(A, B):
            bit_a = 1 << a
            bit_b = 1 << b

            if bit_a & bit_set_1:
                bit_set_2 |= bit_a
                bit_set_2_len += 1
            else:
                bit_set_1 |= bit_a
                bit_set_1_len += 1

            if bit_b & bit_set_1:
                bit_set_2 |= bit_b
                bit_set_2_len += 1
            else:
                bit_set_1 |= bit_b
                bit_set_1_len += 1
            
            answer.append(bit_set_2_len)

        return answer
