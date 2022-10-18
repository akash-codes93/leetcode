/**
 * https://leetcode.com/problems/longest-repeating-character-replacement/
 * overall thinking to the solution can confuse you
 * question will not be solved using a hashmap containing the no of time a variable has come
 *
 * It's a two pointer/ sliding window question but with a twist that you need to iterate over the
 * array 26 times
 *
 * Means For first Iteration consider the question as you can replace and variable in the array with 'A'
 * and find the max len
 *
 * Time: O(26n) == O(n)
 *
 */

let characterReplacement = function (s, k) {
    let total_max_len = 0;
    for (let i = 0; i < 26; i++) {
        let char_to_replace = String.fromCharCode(65 + i);

        let l = 0;
        let r = 0;
        let max_len = 0;
        let current_len = 0;
        let p = k;

        while (l <= r && r < s.length) {

            if (s[r] !== char_to_replace && p > 0) {
                p--;
                current_len++;
                r++;
            } else if (s[r] === char_to_replace) {
                current_len++;
                r++;
            } else if (s[r] !== char_to_replace && p === 0) {

                // case when left is moving which is already 'A'
                if (s[l] !== char_to_replace) {
                    p++;
                }
                // case when l is equal to r
                if (l < r) {
                    current_len--;
                    l++;
                } else {
                    l++;
                    r++;
                }
            }

            if (current_len > max_len) {
                max_len = current_len
            }
        }

        if (max_len > total_max_len) {
            total_max_len = max_len
        }
    }
    return total_max_len;
};


// console.log(characterReplacement('PZBABZB', 2))
// console.log(characterReplacement("AABABBA", 1))
console.log(characterReplacement("ABAA", 0))

