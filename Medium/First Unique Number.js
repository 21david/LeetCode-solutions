/*  
Premium LeetCode problem:

You have a queue of integers, you need to retrieve the first unique integer in the queue.

Implement the FirstUnique class:

FirstUnique(int[] nums) Initializes the object with the numbers in the queue.
int showFirstUnique() returns the value of the first unique integer (integer with a count of 1) of the queue, and returns -1 if there is no such integer.
void add(int value) insert value to the queue.
*/

// TC O(N), SC O(N)
const FirstUnique = function(nums) {
    this.map = {};
    this.queue = [];

    for (let i = 0; i < nums.length; i++) {
        if (nums[i] in this.map)
            this.map[nums[i]] += 1;
        else {
            this.map[nums[i]] = 1;
            this.queue.push(nums[i]);
        }
    }
};

// TC O(N), SC O(1)
FirstUnique.prototype.showFirstUnique = function() {
    for (const number of this.queue)
        if (this.map[number] === 1)
            return number;
    return -1;
};

// TC O(1), SC O(1)
FirstUnique.prototype.add = function(value) {
    if (value in this.map)
        this.map[value] += 1;
    else {
        this.map[value] = 1;
        this.queue.push(value);
    }
};

/*  

M [1, 1, 1]
Q [2, 3, 5]

M [2, 1, 1]
Q [2, 3, 5]

*/

/** 
 * Your FirstUnique object will be instantiated and called as such:
 * var obj = new FirstUnique(nums)
 * var param_1 = obj.showFirstUnique()
 * obj.add(value)
 */
