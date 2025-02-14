class SparseVector:
    def __init__(self, nums: List[int]):
        self.non_zeros_dict = {i: nums[i] for i in range(len(nums)) if nums[i]}

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        # The intersection of the sets tells us which indices
        # have a non-zero value in both vectors. All other indices
        # will have a product of 0.
        intersection = self.non_zeros_dict.keys() & vec.non_zeros_dict.keys()
        dot_product = 0

        for idx in intersection:
            dot_product += self.non_zeros_dict[idx] * vec.non_zeros_dict[idx]

        return dot_product


# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
