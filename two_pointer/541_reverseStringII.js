/**
 * https://leetcode.com/problems/reverse-string-ii/
 */

let reverseStr = (s, k) => {
    s = s.split("")
    let i = 0;
    let count = 0;
    while (i < s.length) {
        let j = (i + k - 1) < s.length ? (i + k - 1) : s.length;
        let p = j;
        if (count % 2 === 0) {
            let c = i + j;
            while (j >= c / 2) {
                let q = s[j]
                s[j] = s[i]
                s[i] = q
                j--;
                i++;
            }
        }
        i = p + 1;
        count += 1
    }
    return s.join("")
};
o = reverseStr("abcdef", 2)
console.log(o)