/**
 * https://leetcode.com/problems/sort-colors/
 */


/**
 * use O(1) extra space
 * use O(n) time
 * @param nums
 */
var sortColors = function(nums) {

    let colors = [0, 0, 0]

    nums.forEach(num => {
        colors[num] += 1
    });

    let i =0;
    colors.forEach((color, index) => {
        while(color !=0 ){
            nums[i] = index
            color--;
            i++;
        }
    })

    return nums
};

o = sortColors([2,0,2,1,1,0])
console.log(o)