/**
 * https://leetcode.com/problems/peak-index-in-a-mountain-array/
 */

var peakIndexInMountainArray = function (arr) {

    let l = 0;
    let r = arr.length - 1;
    let mid = -1

    while (l < r) {
        mid = Math.floor((l + r) / 2);

        let mid_var_prev = arr[mid - 1];
        let mid_var = arr[mid];
        let mid_var_next = arr[mid + 1];
        if (mid_var_prev < mid_var && mid_var < mid_var_next) {
            l = mid
        } else if (mid_var_prev > mid_var && mid_var > mid_var_next) {
            r = mid
        } else {
            return mid
        }
    }

    return mid;
};

// console.log(peakIndexInMountainArray([0, 11, 13, 6, 3, 2, 0]))
// console.log(peakIndexInMountainArray([0, 11, 6, 3, 2, 0]))
// console.log(peakIndexInMountainArray([0, 11, 6, 3, 2, 1, 0]))
// console.log(peakIndexInMountainArray([0, 2,3,4,5,0]))
// console.log(peakIndexInMountainArray([0, 2,3,4,5,6,0]))

