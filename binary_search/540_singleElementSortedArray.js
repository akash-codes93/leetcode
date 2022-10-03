/**
 * https://leetcode.com/problems/single-element-in-a-sorted-array/
 * @param nums
 * time: O(log n)
 * space: O(1)
 */

let singleNonDuplicate = function (nums) {

    let l = 0;
    let r = nums.length - 1;

    while (l <= r) {
        let mid = Math.floor((l + r) / 2);

        if (mid === 0 && nums[mid] !== nums[mid + 1]) {
            return nums[mid]
        } else if (mid === nums.length - 1 && nums[mid] !== nums[mid - 1]) {
            return nums[mid];
        } else if (nums[mid] !== nums[mid - 1] && nums[mid] !== nums[mid + 1]) {
            return nums[mid];
        } else {
            // reducing the halves
            if (nums[mid] === nums[mid - 1]) {
                if (((mid - 1) - l) % 2 !== 0) {
                    r = mid - 2
                } else {
                    l = mid + 1
                }

            } else {
                if ((r - (mid + 1)) % 2 !== 0) {
                    l = mid + 2
                } else {
                    r = mid - 1
                }
            }
        }
    }
};

console.log(singleNonDuplicate([1,1,2,3,3,4,4]))
console.log(singleNonDuplicate([1,1,2,2,3,3,4,6,6]))
console.log(singleNonDuplicate([1,2,2,3,3,4,4]))
console.log(singleNonDuplicate([1,1,2,2,3,3,4]))
console.log(singleNonDuplicate([1,1,2,2,3,3,5,5,7]))
