class Solution:
    def shareCandies(self, candies: List[int], k: int) -> int:
        if k == 0:
            return len(set(candies))

        counts = Counter(candies)
        flavor_count = len(counts)

        # Remove the first k candies
        for i in range(k):
            flavor = candies[i]
            counts[flavor] -= 1
            if counts[flavor] == 0:
                flavor_count -= 1

        max_flavor_amt = flavor_count  # Flavors left over in the window's first position

        # Move window of size k to the right one by one
        # checking if we have more flavors available each time
        for i in range(k, len(candies)):
            oldest = candies[i - k]
            newest = candies[i]

            # Take leftmost candy back
            counts[oldest] += 1 
            if counts[oldest] == 1:  # if we gained a new flavor back
                flavor_count += 1

            # Give rightmost candy away
            counts[newest] -= 1
            if counts[newest] == 0:  # if we lost a flavor
                flavor_count -= 1

            # Check if we have a record amount of flavors
            max_flavor_amt = max(max_flavor_amt, flavor_count)

        return max_flavor_amt
