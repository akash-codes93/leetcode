/**
 * https://leetcode.com/problems/reverse-only-letters/
 */

let reverseOnlyLetters = (s) => {
    let string = s.split("")
    let i = 0;
    let j = s.length - 1;
    while (i < j) {
        if ((s.charCodeAt(i) > 90 || s.charCodeAt(i) < 65) && (s.charCodeAt(i) > 122 || s.charCodeAt(i) < 97)) {
            i++;
        } else if ((s.charCodeAt(j) > 90 || s.charCodeAt(j) < 65) && (s.charCodeAt(j) > 122 || s.charCodeAt(j) < 97)) {
            j--;
        } else {
            let p = string[i]
            string[i] = string[j]
            string[j] = p
            i++;
            j--;
        }
    }
    return string.join('')
};

// o = reverseOnlyLetters("a-bC-dEf-ghIj")
o = reverseOnlyLetters("Test1ng-Leet=code-Q!")
console.log(o)
