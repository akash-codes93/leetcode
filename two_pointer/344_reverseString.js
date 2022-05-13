/**
 * https://leetcode.com/problems/reverse-string/
 * @param s
 */

let reverseString = function (s) {
    let i = 0;
    let len = s.length;
    while (i < len / 2) {
        let p = s[i];
        s[i] = s[len - i - 1]
        s[len - i -1] = p
        i++;
    }
    return s;
};

o = reverseString(["h"])
console.log(o);
