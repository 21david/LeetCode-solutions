# TC = SC = O(V1 + V2)
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        # Convert to integer arrays
        v1 = [int(num) for num in version1.split('.')]
        v2 = [int(num) for num in version2.split('.')]

        V1 = len(v1)
        V2 = len(v2)
        for i in range(max(V1, V2)):
            # Set rev1 to current position. If version1 was too short, set it to 0.
            if i >= V1:
                rev1 = 0
            else:
                rev1 = v1[i]   

            # Set rev2 to current position. If version2 was too short, set it to 0.
            if i >= V2:
                rev2 = 0
            else:
                rev2 = v2[i]  

            # If one is clearly > or <, return. Else, continue to next position.
            if rev1 < rev2:
                return -1
            elif rev1 > rev2:
                return 1
        
        # If all revisions were equal, then the entire versions were equal.
        return 0
