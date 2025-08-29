# TC = SC = O(1)
class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        n_odd = n // 2 + n % 2
        n_even = n // 2

        m_odd = m // 2 + m % 2
        m_even = m // 2

        return n_odd * m_even + n_even * m_odd
        

"""  
n = 5
m = 5

n_odd = 3  (1, 3, 5)
n_even = 2  (2, 4)

m_odd = 3  (1, 3, 5)
m_even = 2  (2, 4)

(1,2)
(1,4)

(2,1)
(2,3)
(2,5)

(3,2)
(3,4)

(4,1)
(4,3)
(4,4)

(5,2)
(5,4)

"""

"""  
3
2

(1,2)

(2,1)

(3,2)
"""
