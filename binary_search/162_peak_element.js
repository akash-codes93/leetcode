/**
 * https://leetcode.com/problems/find-peak-element/
 * @param arr
 * @returns {number}
 */

var findPeakElement = function (arr) {

    // base case
    if (arr.length === 1) {
        return 0
    }

    let l = 0;
    let r = arr.length - 1;
    let mid = -1
    let mid_var_next = -1
    let mid_var_prev = -1

    while (l <= r) {
        mid = Math.floor((l + r) / 2);

        if (mid === 0) {
            mid_var_prev = arr[mid];
        } else {
            mid_var_prev = arr[mid - 1];
        }

        let mid_var = arr[mid];

        if (mid === arr.length - 1) {
            mid_var_next = arr[mid];
        } else {
            mid_var_next = arr[mid + 1];
        }

        if (mid_var_prev <= mid_var && mid_var < mid_var_next) {
            l = mid + 1
        } else if (mid_var_prev > mid_var && mid_var >= mid_var_next) {
            r = mid - 1
        } else if (mid_var_prev > mid_var && mid_var < mid_var_next) {
            if (mid_var_prev > mid_var_next) {
                r = mid - 1
            } else {
                l = mid + 1
            }

        } else {
            return mid
        }
    }

    return mid;
};

// console.log(findPeakElement([0, 11, 13, 6, 3, 2, 0]))
// console.log(findPeakElement([0, 11, 6, 3, 2, 0]))
// console.log(findPeakElement([0, 11, 6, 3, 2, 1, 0]))
// console.log(findPeakElement([0, 2,3,4,5,0]))
// console.log(findPeakElement([0, 2,3,4,5,6,0]))
// console.log(findPeakElement([3, 2, 1]))
// console.log(findPeakElement([1, 2, 1, 3, 5, 6, 4]))
// console.log(findPeakElement([1]))
// console.log(findPeakElement([1, 2]))
// console.log(findPeakElement([3, 1, 2]))
console.log(findPeakElement([5, 2, 1, 2, 9]))