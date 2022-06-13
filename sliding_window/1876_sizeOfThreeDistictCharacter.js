/**
 * https://leetcode.com/problems/substrings-of-size-three-with-distinct-characters/
 */

let countGoodSubstrings = (s) => {
    let i = 0;
    let j = 2;
    let count = 0;

    while (j < s.length) {
        let unique = new Set()
        let subCount = 0
        let begin = i
        while (begin <= j) {
            if (unique.has(s[begin])) {
                break
            }
            unique.add(s[begin])
            subCount++;
            begin++;
        }
        if (subCount === 3) {
            count++;
        }
        i++;
        j++;
    }
    return count
};

o = countGoodSubstrings("xyzzaz")
console.log(o)
