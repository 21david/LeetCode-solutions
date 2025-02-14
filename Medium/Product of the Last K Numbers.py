""" 
Keep a prefix product array. To get the product of the last
k numbers, divide the current accumulated product by the (k-1)th 
last product. The array should always start with a 1 which represents
an empty subarray. It allows us to calculate the product of the
entire array if k is asking for all the previous numbers.
See below:
Let's say we add 3, 1, 2, 5, and 4 (5 integers in total).
nums = [3,1,2,5,4]
prefix_prof = [1, 1*3, 1*3*1, 1*3*1*2, 1*3*1*2*5, 1*3*1*2*5*4]

if k = 2, divide nums[-1] by nums[-3] (or nums[-1 - 2]):

    1*3*1*2*5*4
    -----------
    1*3*1*2

    = 5 * 4

if k = 5, divide nums[-1] by nums[-1 - 5]:

    1*3*1*2*5*4
    -----------
    1

    = 3 * 1 * 2 * 5 * 4

Since a 0 messes up the prefix product array, we can reset the prefix
product array when we get a 0. We can tell if a call to get_product
will include this 0 by comparing the size of the array with k. If k
asks for more than the current size of the array, then it's trying to
include the last 0, so we can just return 0. Otherwise, we can calculate
the product as normal and return it.
"""
class ProductOfNumbers:

    # O(1)
    def __init__(self):
        self.prefix_prod = [1]
        self.curr_prod = 1

    # O(1)
    def add(self, num: int) -> None:
        if num == 0:
            self.__init__()
            return

        self.curr_prod *= num
        self.prefix_prod.append(self.curr_prod)

    # O(1)
    def getProduct(self, k: int) -> int:
        if k > len(self.prefix_prod) - 1:
            return 0

        return self.curr_prod // self.prefix_prod[-1 - k]

# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
