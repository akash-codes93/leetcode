/**
 * https://leetcode.com/problems/intersection-of-two-arrays-ii/
 */

let intersect = (nums1, nums2) => {
    nums1 = nums1.sort((a, b) => a - b);
    nums2 = nums2.sort((a, b) => a - b);
    let i = 0;
    let j = 0;

    let intersect = [];

    while (i < nums1.length && j < nums2.length) {
        if (nums1[i] === nums2[j]) {
            intersect.push(nums1[i])
            i++;
            j++;
        } else if (nums1[i] > nums2[j]) {
            j++;
        } else {
            i++;
        }

    }
    return intersect;

};

o = intersect(nums1 = [1, 2, 2, 1, 2, 1, 3], nums2 = [2, 2, 3, 3, 3, 2])
console.log(o)
