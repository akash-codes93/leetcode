/**
 * https://leetcode.com/problems/longest-nice-substring/
 * eg. YazaAay
 * :: its divide and conquer problem
 * :: not easy for sure
 */

let findOtherChar = (i, s) => {
    if (s.charCodeAt(i) >= 65 && s.charCodeAt(i) <= 90) {
        return s[i].toLowerCase();
    } else {
        return s[i].toUpperCase();
    }
}


let longestNiceSubstring = (s) => {
    if (s.length < 2) {
        return ""
    }

    let distinct_elements = new Set();
    for (let i = 0; i < s.length; i++) {
        distinct_elements.add(s[i]);
    }

    for (let i = 0; i < s.length; i++) {
        if (distinct_elements.has(findOtherChar(i, s))) {

        }
        else{
            let s1 = longestNiceSubstring(s.substring(0, i));
            let s2 = longestNiceSubstring(s.substring(i+1, s.length));
            return s1.length > s2.length ? s1 : s2
        }
    }
    return s
};


o = longestNiceSubstring("dDzeE");
// o = findOtherChar(2, "YazAay");
console.log(o)
