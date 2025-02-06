"""
Every set of numbers (a, b, c, d) such that A * B == C * D produces eight 
permutations in total, which can be thought of as 2 * 2 * 2. The first two 
represent flipping A and B, the second two represent flipping C and D, and the 
third two represent flipping the pairs so that it's C * B == A * B and all the 
equivalent permutations.

What we can do is calculate the product of every pair of two numbers and then 
count the frequency of each of those products in a dictionary. We do this 
because if a product has a frequency of at least two, then that means we can 
extract an A and a B, and a C and a D from it. If a product only had a frequency 
of one in the dictionary, then that means there was only an A and a B but no 
equivalent C and D.

Once we've calculated all the possible products, we go through all of them in 
the dictionary. For all of the ones that had a frequency of two or more, we add 
the number of tuples we can extract from it to the answer. If it has a frequency 
of two, then there are eight tuples, as explained above, so we add 8 to the 
answer to get the amount.

If there's more than two, we can visualize it as a graph. For example, if the 
product has a frequency of three, then we can think of this as a graph with 
three nodes. We want all the tuples from each pair of two nodes in this graph, 
so it is a complete graph where every node connects to every other node. There 
are three edges in this case. Each edge represents an A * B == C * D, which 
comes with 8 tuples in total. So, we add three times eight to the final answer.

As we add more nodes, the number of edges increases, like the numbers in the 
triangle numbers. To calculate that, we take the number of nodes and apply the 
formula n * (n - 1) / 2, which gives us the number of edges in a complete graph. 
We then multiply that number of edges by 8 to figure out how many more tuples we 
can extract.

TC = SC = O(N^2)
"""
class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        N = len(nums)

        # Multiply every element times every other element, and count the frequency of their products
        product_counts = defaultdict(int)
        for i in range(N - 1):
            for j in range(i + 1, N):
                num1, num2 = nums[i], nums[j]
                product_counts[num1 * num2] += 1

        # Count how many tuples we can make using the dictionary
        ans = 0
        for product, freq in product_counts.items():
            if freq >= 2:
                edges = (freq) * (freq - 1) // 2
                ans += edges * 8

        return ans
