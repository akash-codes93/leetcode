/**
 * https://leetcode.com/problems/subarray-product-less-than-k/
 *
 * Medium:: these questions does not have equality
 * Two pointer problem
 * no prefix sum
 * T = O(n)
 * S = O(1)
 */

let numSubarrayProductLessThanK = function (nums, k) {
    let product = 1;
    let l = 0;
    let r = 0;
    let cnt = 0

    while (r < nums.length && l <= r) {
        product = product * nums[r];

        if (product < k) {
            let size = r - l + 1
            cnt += size
            r++;
        } else {
            product = product / nums[l];
            if(l !== r){
                product = product / nums[r];
            }
            if(l===r){
                l++;
                r++;
            }
            else{
                l++;
            }
        }


    }
    return cnt
};

console.log(numSubarrayProductLessThanK([10, 5, 2, 6], 100))
console.log(numSubarrayProductLessThanK([1, 2, 3], 0))
console.log(numSubarrayProductLessThanK([2, 1, 2, 3, 4], 5))
console.log(numSubarrayProductLessThanK([57, 44, 92, 28, 66, 60, 37, 33, 52, 38, 29, 76, 8, 75, 22], 18))
