/**
 * https://leetcode.com/problems/3sum/
 */


/**
 * time: O(n^2)
 * space: O(1)
 * @param nums
 * for every element you find two element that sum is zero
 * !(j-1 > i && nums[j] === nums[j-1] && nums[k] === nums[k+1]) condition to avoid duplicates
 */
let threeSum = (nums) => {

    nums = nums.sort((a, b) => a - b);
    // console.log(nums);
    let ans = [];

    for (let i = 0; i < nums.length; i++) {

        if (i === 0) {

        } else if (nums[i] === nums[i - 1]) {
            continue
        }

        let j = i + 1;
        let k = nums.length - 1;

        while (j < k) {
            if (nums[i] + nums[j] + nums[k] === 0) {
                // console.log(i,j,k)
                if (!(j-1 > i && nums[j] === nums[j-1] && nums[k] === nums[k+1])) {
                    ans.push([nums[i], nums[j], nums[k]])
                }
                k--;
                j++;
            } else if (nums[i] + nums[j] + nums[k] > 0) {
                k--;
            } else {
                j++;
            }
        }
    }
    return ans;
};

// o = threeSum([-1,0,1,2,-1,-4])
// o = threeSum([0,0,0])
// o = threeSum([])
o = threeSum([-2, -2, 0, 0, 0, 2, 2, 2])
console.log(o);
