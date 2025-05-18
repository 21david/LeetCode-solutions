/*  
After watching Neetcode video

We need to calculate the size of half the array if even. 
If odd, it's half not including the middle element.
We can binary search on one. On each iteration, we take up to the current number
in the first array, then take the remaining elements we need to get half the total
number of elements from the other array, taking the leftmost elements.

We need to check if these selected elements form exactly the first half of the total array.
We can do this by checking if the maximum of the rightmost selected elements (from both arrays)
is less than the minimum of both the next elements. If so, then we have the first half.

If there are an odd number of total elements, then the median is the minimum of the two next elements.
If there are an even number of total elements, then the median is the maximum of the selected elements,
plus the minimum of the two next elements, divided by 2.

This binary search can be done on either array I believe. This is because, let's say you color each cell
either red or blue. Red means it belongs to the first half, blue to the second half (lets say odd middle
element stays uncolored). There will be one element that is the last one of its color (going left to right).
We are just binary searching for that element. We can determine the remaining elements in the other array
using math and logic in O(1).

Therefore I think it's best to do it on the smallest array to reduce work.

TC = O(log(min(N, M)))
SC = O(1)
*/

function findMedianSortedArrays(nums1: number[], nums2: number[]): number {
    let [N1, N2] = [nums1.length, nums2.length];
    let total = N1 + N2;
    let evenTotal = total % 2 === 0;

    // Empty array edge case
    if (N1 === 0) {
        // return median of second array
        if (evenTotal)
            return (nums2[N2 / 2] + nums2[N2 / 2 - 1]) / 2;
        else
            return nums2[Math.floor(N2 / 2)];

    } else if (N2 === 0) {
        // return median of first array
        if (evenTotal)
            return (nums1[N1 / 2] + nums1[N1 / 2 - 1]) / 2;
        else
            return nums1[Math.floor(N1 / 2)];
    }

    // Put the smaller array into nums1
    if (N2 < N1) {
        [nums1, nums2] = [nums2, nums1];
        [N1, N2] = [N2, N1];
    }

    let half = Math.floor(total / 2);

    // BS on nums 1
    let lo = 0;
    let hi = nums1.length - 1;
    let mid;
    let otherIdx, left1, left2;
    let right1 = 0, right2;
    while (true) {
        mid = Math.floor((hi + lo) / 2); // lo + Math.floor((hi - lo) / 2);
        otherIdx = half - (mid + 1) - 1; // half - mid - 2

        left1 = mid >= 0? nums1[mid] : -Infinity;
        right1 = (mid + 1) < N1? nums1[mid + 1] : 1000000000;
        left2 = otherIdx >= 0? nums2[otherIdx] : -Infinity;
        right2 = (otherIdx + 1) < N2? nums2[otherIdx + 1] : Infinity;

        if (left1 <= right2 && left2 <= right1) {
            if (evenTotal)
                return (Math.max(left1, left2) + Math.min(right1, right2)) / 2;
            else
                return Math.min(right1, right2);
        } else if (left1 > right2) {
            hi = mid - 1;
        } else {
            lo = mid + 1;
        }
    }
};

// Solved after seeing neetCode's code
