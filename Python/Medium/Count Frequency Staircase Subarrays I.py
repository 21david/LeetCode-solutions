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
                    
            
