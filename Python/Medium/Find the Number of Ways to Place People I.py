# TC = O(N^3). 
    # 50^3 = 125,000 = 1.25 * 10 ^ 5, which is below usual limit of ~10^8 that LC can handle
# SC = O(1)
class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        ans = 0

        for x1, y1 in points:
            for x2, y2 in points:
                if (x1,y1) == (x2,y2): 
                    # Prevent it from considering itself
                    continue  

                if not (x1 <= x2 and y1 >= y2):
                    # Only points where (x1,y1) is on upper left side of (x2,y2), 
                    # including vertically and horizontally
                    continue  

                # Check that every other point isn't in the rectangle
                valid = True
                for x3, y3 in points:
                    # Only consider new points
                    if (x3,y3) in [(x1,y1), (x2,y2)]: continue  

                    # If (x3,y3) is in between the two points, then these two points aren't valid
                    if (x1 <= x3 <= x2) and (y1 >= y3 >= y2):
                        valid = False
                        break
                
                ans += valid  # Add 1 if no point was in the rectangle of (x1,y1) and (x2,y2)

        return ans
