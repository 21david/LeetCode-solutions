# TC = O(NlogN) due to sorting
# SC = O(N)
class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        # multiset to store counts of each distinct number
        cts = Counter(nums)

        ans = []

        while True:
            temp = []
            # Mechanism to stop loop once there are no more numbers
            found_one = False
            
            # Gather one of each distinct number, sort, and append
            for k, v in cts.items():
                if cts[k] >= 1:
                    found_one = True
                    temp.append(k)
                    cts[k] -= 1
            temp.sort()
            ans.extend(temp)

            if not found_one:
                break

        return ans
            
