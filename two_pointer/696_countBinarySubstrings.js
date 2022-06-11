/*
 * @url: https://leetcode.com/problems/count-binary-substrings/
 * find groups of zeros and one
 * min(countZero, countOne)
 *
 * 00001110011
 *
 * groups are
 * 0000111 => min(4,3) = 3
 * 11100 => min(3,2) = 2
 * 0011 => min(2,2) = 2
 * total = 7
 */

let countBinarySubstrings = function (s) {

    let curr = 1;
    let prev = 0;
    let count = 0;

    for (let i = 1; i < s.length; i++) {
        if(s[i] !== s[i-1]){
            count += Math.min(curr, prev)
            prev = curr
            curr = 1

        }else{
            curr ++;
        }
    }
    count += Math.min(curr, prev)
    return count
};

o = countBinarySubstrings("00001110011")
console.log(o)