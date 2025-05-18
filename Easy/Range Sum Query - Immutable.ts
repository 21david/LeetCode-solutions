class NumArray {
    private prefixSum: number[];
    
    constructor(nums: number[]) {
        this.prefixSum = [0];
        let acc = 0;
        for (let num of nums) {
            acc += num;
            this.prefixSum.push(acc);
        }
    }

    sumRange(left: number, right: number): number {
        return this.prefixSum[right + 1] - this.prefixSum[left];
    }
}

/**
 * Your NumArray object will be instantiated and called as such:
 * var obj = new NumArray(nums)
 * var param_1 = obj.sumRange(left,right)
 */
