/**
 * https://leetcode.com/problems/remove-element/
 */

let removeElement = (nums, val) => {
    let i = 0;
    let j = -1;

    while (i < nums.length) {
        if (nums[i] === val) {
            if (j === -1) {
                j = i
            }
        } else {
            if (j !== -1) {
                nums[j] = nums[i]
                j++;
            }
        }
        i++;
    }
    return j === -1 ? nums.length : j  // missed this!
};

// o = removeElement([2, 3, 2, 1, 3, 5, 4], 3)
o = removeElement([2], 3)
console.log(o)
