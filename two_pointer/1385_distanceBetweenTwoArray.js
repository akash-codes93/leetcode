/**
 * https://leetcode.com/problems/find-the-distance-value-between-two-arrays/
 * sort other array and use binary search
 * O(m log n) + O(n log n)
 */

let findElementDistance = (nums, num, d) => {
    let left = 0;
    let right = nums.length - 1;
    let mid = 0;
    while (left <= right) {
        mid = parseInt((left + right) / 2)
        if (num === nums[mid]) {
            return 0
        } else if (num > nums[mid]) {
            left = mid + 1
        } else {
            right = mid - 1
        }
    }
    mid = parseInt((left + right)/2)
    if (nums[mid] > nums) {
        left = mid
        right = mid
    } else {
        left = mid
        right = mid + 1
    }
    if (Math.abs(num - nums[left]) <= d || Math.abs(num - nums[right]) <= d) {
        return 0;
    } else {
        return 1;
    }
}


let findTheDistanceValue = function (arr1, arr2, d) {
    arr2 = arr2.sort((a, b) => a - b);
    console.log(arr2)
    let count = 0;
    for (let i = 0; i < arr1.length; i++) {
        count += findElementDistance(arr2, arr1[i], d)
    }

    return count
};

// o = findTheDistanceValue(arr1 = [4,5,8], arr2 = [10,9,1,8], d = 2)
// o = findTheDistanceValue(arr1 = [1, 4, 2, 3], arr2 = [-4, -3, 6, 10, 20, 30], d = 3)
// o = findTheDistanceValue(arr1 = [2,1,100,3], arr2 = [-5,-2,10,-3,7], d = 6)
// o = findTheDistanceValue(
//     [-803, 715, -224, 909, 121, -296, 872, 807, 715, 407, 94, -8, 572, 90, -520, -867, 485, -918, -827, -728, -653, -659, 865, 102, -564, -452, 554, -320, 229, 36, 722, -478, -247, -307, -304, -767, -404, -519, 776, 933, 236, 596, 954, 464],
//     [817, 1, -723, 187, 128, 577, -787, -344, -920, -168, -851, -222, 773, 614, -699, 696, -744, -302, -766, 259, 203, 601, 896, -226, -844, 168, 126, -542, 159, -833, 950, -454, -253, 824, -395, 155, 94, 894, -766, -63, 836, -433, -780, 611, -907, 695, -395, -975, 256, 373, -971, -813, -154, -765, 691, 812, 617, -919, -616, -510, 608, 201, -138, -669, -764, -77, -658, 394, -506, -675, 523, 730, -790, -109, 865, 975, -226, 651, 987, 111, 862, 675, -398, 126, -482, 457, -24, -356, -795, -575, 335, -350, -919, -945, -979, 611],
//     37
// )
console.log(o)
