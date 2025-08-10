# After seeing hint: "Take the bitwise AND of all elements that are not in their correct position."
# TC = O(N)
# SC = O(1)
class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        MAX_INT = 2 ** 31 - 1
        ans = MAX_INT
        N = len(nums)
        for i in range(N):
            curr = nums[i]
            if curr != i:
                ans &= curr
        return ans if ans != MAX_INT else 0

# Same as above, using reduce
# TC = O(N)
# SC = O(1)
class Solution2:
    def sortPermutation(self, nums: List[int]) -> int:
        MAX_INT = 2 ** 31 - 1
        accumulated_and = reduce(operator.and_, (num for i, num in enumerate(nums) if num != i), MAX_INT)
        return accumulated_and if accumulated_and != MAX_INT else 0

# My original solution
# TC = O(N), check if each number is out of order, then O(1) to iterate through bits array and calculate answer
    # Technically O(N log U), where U is the highest number, since we have to check each of its bits 
    # (inner "while curr loop"), but since the highest number is bound by 10^5, it becomes a constant (~17), 
    # so this function actually runs in O(N).
# SC = O(1)
class Solution3:
    def sortPermutation(self, nums: List[int]) -> int:
        if (nums[0] != 0) or (len(nums) <= 2):
            return 0  # 0 must be in place otherwise only k = 0 puts it back in place

        # Create array of 17 bits (max number of bits for numbers <= 10^5)
        # and count frequency of each bit in each number that is not in the index 
        # its supposed to be in
        NUM_BITS = 17
        bits = [0] * NUM_BITS
        N = len(nums)
        num_out_of_order = 0
        for i in range(N):
            curr = nums[i]
            if curr != i:
                num_out_of_order += 1
                # add bits to bits array
                b = 0
                while curr:
                    bits[b] += curr & 1
                    curr >>= 1
                    b += 1

        # print(num_out_of_order)
        # print(bits)

        # The answer should set the bits that were also set in each of the numbers
        # that weren't in their final sorted index (in num_out_of_order). I later realized this was the
        # equivalent of ANDing all of those numbers.
        ans = 0
        bit = 1
        for i in range(NUM_BITS):
            if bits[i] == num_out_of_order:
                # If all numbers had this bit set, set it in answer
                ans |= bit

            bit <<= 1

        return ans

        
"""
Test cases:
[0,3,2,1]
[0,1,3,2]
[3,2,1,0]

[0,2,3,4,1] => 0
[0,5,2,1,4,3] => 1

[0,2,3,4,1]
[0,5,2,1,4,3]
[0]
[0,1]
[1,0]
[0,1,2]
[0,2,1]
[1,2,0]
"""
