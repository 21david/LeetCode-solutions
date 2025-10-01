class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans = numBottles  # Should always drink all at the start

        # numBottles will store the current number of bottles we have on hand

        # While we can still get new bottles
        while numBottles // numExchange:
            # Calculate new bottles we can get, store remainder ones
            new, rem = divmod(numBottles, numExchange)

            # Drink the new bottles
            ans += new

            # Now we have the new empty bottles plus the previous remainder empty bottles
            numBottles = new + rem

        return ans

# TC = O(log B), or "log base numExchange (numBottles)"", aka "log numBottles" where the base is numExchange
# SC = O(1)
