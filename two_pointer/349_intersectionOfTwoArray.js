/**
 * https://leetcode.com/problems/intersection-of-two-arrays/
 */

/**
 * Example 1:
 * Input: nums1 = [1,2,2,1], nums2 = [2,2]
 * Output: [2]
 *
 *  Example 2:
 * Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
 * Output: [9,4]
 * Explanation: [4,9] is also accepted.
 *
 * @param nums1
 * @param nums2
 */

let intersection = function(nums1, nums2) {
    let nums3 = new Set(nums2)
    let nums4 = [];
    for(let i=0; i< nums1.length; i++){
        if(nums3.has(nums1[i])){
            nums4.push(nums1[i])
        }
    }
    return new Set(nums4)
};

o = intersection([1,2,2,1], [2,2])
console.log(o)