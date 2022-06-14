/**
 * https://leetcode.com/problems/find-the-k-beauty-of-a-number/
 */

let divisorSubstrings = function(num, k) {

    let nums = num.toString()
    let i = 0;
    let j = i + k - 1;
    let count = 0

    while (j < nums.length){
        let subInt = parseInt(nums.substring(i, j+1))
        if(num % subInt === 0){
            count++;
        }
        i++;
        j++;
    }
    return count
};

o = divisorSubstrings(240, 2)
console.log(o)
