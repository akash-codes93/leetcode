/**
 * https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/
 */

var longestSubarray = function (s) {

    let i = 0;
    let j = 0;
    let longest_length = 0;
    let cur_len = 0;
    let to_del = 1;

    while (j < s.length) {

        if (s[j] === 0) {
            if (to_del === 1) {
                to_del -= 1
            } else {
                i = i + 1;
                j = j -1
                cur_len = 0;
                if(s[i-1] === 0)
                    to_del = 1
            }
        }
        cur_len = (j - i) - (1 - to_del) + 1


        if (cur_len > longest_length) {
            longest_length = cur_len
        }

        j++;
    }

    if (i ===0 && j === s.length && to_del === 1) {
        longest_length--;
    }

    return longest_length
};

// o = longestSubarray([1, 1, 0, 1])
// o = longestSubarray([1, 1, 0, 0, 1, 0, 1, 1, 1])
// o = longestSubarray([0,1,1,1,0,1,1,0,1])
o = longestSubarray([1,1,1,1,1,1])
console.log(o);
