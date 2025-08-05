class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        unplaced = 0
        for fruit in fruits:
            found = False
            # Look for the leftmost basket that can fit current fruits
            for i in range(len(baskets)):
                if baskets[i] >= fruit:
                    baskets[i] = 0
                    found = True
                    break

            # If none could fit, this one remains unplaced
            if not found:
                unplaced += 1

        return unplaced
