'''
Sliding window approach with a fixed size window.

Maintain a map that stores the numbers in the current window position and their frequency count.
After each iteration of sliding the window, the length/size of the map tells us how
many distinct characters there are at that position. We use that for the final answer.
Then, to move the window, we remove the oldest number (leftmost side of the window)
and add the newest number (rightmost side of the window), by modifying the counts in the
map. If a number reaches 0 count, we delete it from the map to make sure the length/size is accurate.

TC: O(N)
Auxilliary SC: O(K)
'''
class Solution:
    def distinctNumbers(self, nums: List[int], k: int) -> List[int]:
        N = len(nums)
        answer = [0] * (N - k + 1)
        current_numbers_map = Counter(nums[:k])

        for i in range(k, N):
            # Set the current number of distinct numbers
            answer[i - k] = len(current_numbers_map)

            # Now remove oldest number and add the newest number
            oldest_num = nums[i - k]
            newest_num = nums[i]

            current_numbers_map[oldest_num] -= 1
            if current_numbers_map[oldest_num] == 0:
                del current_numbers_map[oldest_num]

            current_numbers_map[newest_num] = current_numbers_map.get(newest_num, 0) + 1

        # Fill in the last one which isn't covered by the loop
        answer[-1] = len(current_numbers_map)

        return answer
