class Solution:
    def findLucky(self, arr: List[int]) -> int:
        cts = list(Counter(arr).items())
        cts.sort(key = lambda x: -x[0])
        # print(cts)
        for num, freq in cts:
            if num == freq:
                return num
        return -1
        
