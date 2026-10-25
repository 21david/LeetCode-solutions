class Solution:
    def countStaircase(self, nums: list[int]) -> int:
        N = len(nums)
        ans = N
        
        for s in range(N-2):
            curr_frequencies = [1]
            max_frequencies = {nums[s]: 0}
            distincts = 1 
            
            for e in range(s+1, N):
                if nums[e] not in max_frequencies:
                    max_frequencies[nums[e]] = distincts
                    distincts += 1
                    curr_frequencies.append(1)
                else:
                    idx = max_frequencies[nums[e]]
                    curr_frequencies[idx] += 1
                    if curr_frequencies[idx] > idx + 1:
                        # This number's frequency is too high so a staircase wont be possible anymore
                        break
                    
                # Check if we have a staircase
                staircase = True
                for j in range(1, len(curr_frequencies)):
                    if curr_frequencies[j] != curr_frequencies[j-1] + 1:
                        staircase = False
                        break

                ans += staircase

        return ans
                    

'''
More optimal:
we can do a nested loop
if all these are satisfied, then we have a staircase:
- we have k distinct numbers
    - if k becomes > 316, we can break the inner loop because the expected length would be
        greater than 50,000 which is the max length for nums
- we have k*(k+1)/2 length subarray
    - we can compute at end of each iteration in O(1)
- none of the frequencies are higher than their max
    - we can check when adding each new number in O(1)

TC = O(N sqrt N)
'''
class Solution:
    def countStaircase(self, nums: list[int]) -> int:
        N = len(nums)
        ans = N  # include all the 1-length subarrays from the start

        for s in range(N-2):
            distincts = 1
            max_frequencies = { nums[s]: 1 }
            curr_frequencies =  { nums[s] : 1 }
            expected_length = 1
            
            for e in range(s+1, N):
                if nums[e] not in max_frequencies:
                    distincts += 1
                    if distincts > 316:
                        break
                    max_frequencies[nums[e]] = distincts

                    # only when we get a new distinct number do we update expected_length length
                    expected_length = distincts * (distincts +1) // 2
                    curr_frequencies[nums[e]] = 0
                
                curr_frequencies[nums[e]] += 1

                if curr_frequencies[nums[e]] > max_frequencies[nums[e]]:
                    # it overshot, move to the next starting point for a subarray
                    break

                # if no overshooting, and length of current subarray gives expected_length length
                # for a perfect staircase array, then we have a staircase
                if expected_length == (e - s + 1):
                    ans += 1
                
        return ans
