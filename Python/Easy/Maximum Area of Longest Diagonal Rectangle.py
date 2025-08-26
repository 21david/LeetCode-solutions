class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        def diag(a, b):
            return sqrt(a ** 2 + b ** 2)

        # Sort by diagonal, ascending, and for ties, sort by area, ascending
        # Answer should be the last element after this
        dimensions.sort(key = lambda dim: ( diag(*dim) , dim[0] * dim[1] ))

        return dimensions[-1][0] * dimensions[-1][1]
