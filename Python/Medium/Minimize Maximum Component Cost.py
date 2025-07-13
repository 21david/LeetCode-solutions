class Solution:
    def minCost(self, n: int, edges: List[List[int]], k: int) -> int:
        if n == 1 or n == k: return 0

        edges.sort(key = lambda x: x[-1])

        '''
        Go through each edge from smallest to largest.
        Initialy, through this method, all nodes will be their own component.
        So there will be n components total.
        We will go through each edge in order starting from smallest.
        Each union() will connect two components, and the total number of components
        will fall little by little.
        Union() can tell us if we connected two components or not, to update the count.
        Once the total number of components reaches
        k, then we take the maximum edge we'ev seen so far. 
        '''

        uf = UF(n)
        connComp = uf.connected_components

        # Go through each edge from smallest to largest. After each one, if number of connected
        # components is k, then the answer is the last edge we added, as that is the largest one.
        i = 0
        while connComp > k:
            currEdge = edges[i]
            connComp = uf.union(currEdge[0], currEdge[1])
            i += 1

        return edges[i-1][-1]


class UF:
    def __init__(self, n):
        self.king = list(range(n))
        self.size = [1] * n
        self.connected_components = n

    def find(self, x):
        if x != self.king[x]:
            self.king[x] = self.find(self.king[x])
        return self.king[x]

    def union(self, x, y):
        kingX = self.find(x)  # find 'king' of x's group
        kingY = self.find(y)

        if kingX != kingY:
            # They are not already in the same group, so the 
            # total number of components goes down
            self.connected_components -= 1
            if self.size[kingX] < self.size[kingY]:
                self.king[kingX] = kingY
                self.size[kingY] += self.size[kingX]
            else:
                self.king[kingY] = kingX
                self.size[kingX] += self.size[kingY]

        return self.connected_components

'''
tests
5
[[0,1,4],[1,2,3],[1,3,2],[3,4,6]]
2
4
[[0,1,5],[1,2,5],[2,3,5]]
1
8
[[6,7,6],[1,2,4],[4,7,10],[5,3,9],[4,6,8],[7,5,6],[1,4,5],[1,5,5],[0,1,3]]
3
1
[]
1
2
[[0,1,4]]
2
3
[[0,1,4],[1,2,10]]
2

'''
