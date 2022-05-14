/*
https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-string-balanced/
 */

let minSwaps = function (s) {
    let swaps = 0;
    let string = s.split("")
    let left = -1;
    let right = s.length;
    let left_sum = 0;
    let right_sum = 0;

    while (left < right) {
        if (left_sum >= 0) {
            left++;
            if (string[left] === '[' ) {
                left_sum++;
            } else {
                left_sum--;
            }
        }
        if (right_sum <= 0) {
            right--;
            if (string[right] === '[') {
                right_sum++;
            } else {
                right_sum--;
            }
        }
        if (left_sum < 0 && right_sum > 0) {
            let p = string[left];
            string[left] = string[right];
            string[right] = p;
            swaps++;
            left_sum += 2;
            right_sum -= 2;
        }
        console.log(left, right)
    }

    return swaps;

};

// o = minSwaps("[[]]]]]]]][[[[[]][[[][][][")
// o = minSwaps("][][")
o = minSwaps("][")
// o = minSwaps("[]")
// o = minSwaps("]]][[[")
console.log(o)