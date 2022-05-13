/*
https://leetcode.com/problems/reverse-words-in-a-string-iii/
 */

var reverseWords = function (s) {
    var length = s.length;
    var array = s.split("")
    var left = 0
    var right = 0
    while (right < length) {
        if (array[right] === ' ' || right === length-1) {
            if(array[right] === ' '){
                var k = right-1
            }
            else{
                var k = right
            }

            // console.log(left, right)
            while (left < (k+left) / 2) {
                // console.log(s[left], s[k])
                let p = array[left]
                array[left] = s[k]
                array[k] = p

                left++;
                k--;
            }
            left = right + 1
        }
        right++;
    }
    // console.log(array)
    return array.join("")
};

o = reverseWords("Let's take LeetCode contest")
console.log(o)