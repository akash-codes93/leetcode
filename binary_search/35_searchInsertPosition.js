/**
 * https://leetcode.com/problems/search-insert-position/
 * nums:: sorted and distinct element
 */

let searchInsert = function (nums, target) {

    //base case
    if (target < nums[0]) {
        return 0;
    }
        // else if (target === nums[0]) {
        //     return 1;
    // }
    else if (target === nums[nums.length - 1]) {
        return nums.length - 1;
    } else if (target > nums[nums.length - 1]) {
        return nums.length;
    }

    let l = 0;
    let r = nums.length - 1;

    while (l <= r) {
        let mid = Math.floor((l + r) / 2);

        if (target === nums[mid]) {
            return mid
        } else if (target > nums[mid] && target < nums[mid + 1]) {
            return mid + 1;
        } else if (target >= nums[mid + 1]) {
            l = mid;
        } else {
            r = mid;
        }
    }
};

/**
# python solution
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return bisect.bisect_left(nums, target)

**/

console.log(searchInsert([1, 3, 8, 15, 67], 50))
console.log(searchInsert([1, 3, 8, 15, 67], 15))
console.log(searchInsert([1, 3, 8, 15, 67], 10))
console.log(searchInsert([1, 3, 8, 15, 67], 58))
console.log(searchInsert([1, 3, 8, 15, 67], 0))
console.log(searchInsert([1, 3, 8, 15, 67], 2))
console.log(searchInsert([1, 3, 8, 15, 67, 100], 30))
console.log(searchInsert([1, 3, 8, 15, 67, 100], 50))
console.log(searchInsert([1, 3, 8, 15, 67, 100], 102))


