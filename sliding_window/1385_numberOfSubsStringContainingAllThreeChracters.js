/**
 * https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/
 * @param {string} s
 * @return {number}
 * make a window i, j and an array of abc count
 * as you encounter abc in i, j you know rest of the string will always have abc substring
 */

let numberOfSubstrings = (s) => {
    let counts = {
        'a': 0,
        'b': 0,
        'c': 0
    };
    let i = 0;
    let j = 1;

    let total = 0
    counts[s[i]] = 1

    while(i < s.length){

        counts[s[j]] += 1

        if(counts['a'] >=1 && counts['b'] >= 1 && counts['c'] >= 1){
            total += s.length - j;
            counts[s[i]] -= 1
            i ++;
            counts[s[j]] -= 1
            j --;
        }
        else if (j === s.length-1){
            counts[s[i]] -= 1
            i++
        }
        if(j < s.length-1){
            j++;
        }

    }

    return total

};

// o = numberOfSubstrings("abcabc");
// o = numberOfSubstrings("abc");
// o = numberOfSubstrings("aaacb")
// o = numberOfSubstrings("ababbbc")
// o = numberOfSubstrings("acbbcac")
console.log(o);
