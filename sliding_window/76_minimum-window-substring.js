/**
 * https://leetcode.com/problems/minimum-window-substring/
 * Hard
 * solved own
 */

let findFrequency = str => {
    let freq = {}
    for (let i = 0; i < str.length; i++) {
        if (str[i] in freq) {
            freq[str[i]] += 1
        } else {
            freq[str[i]] = 1
        }
    }
    return freq
}

// let minWindow = function (s, t) {

/**
 * This solution will give a substring containing all characters from t
 * but this substring will not be the minimum
 */

//     if (t.length > s.length) {
//         return ""
//     }
//
//     let freq_s = findFrequency(s);
//     let freq_t = findFrequency(t);
//
//     let max_pos = {};
//     for (let i = 0; i < s.length; i++) {
//         max_pos[s[i]] = i
//     }
//     console.log(freq_s, freq_t, max_pos)
//     let max_len = 0;
//     for (let i = 0; i < t.length; i++) {
//         if (!(t[i] in max_pos)) {
//             return ""
//         }
//
//         if (max_pos[t[i]] > max_len){
//             max_len = max_pos[t[i]];
//         }
//     }
//     console.log(max_len)
//     let l = 0;
//
//     while(l < max_len) {
//         if (!(s[l] in freq_t)){
//             l++;
//         }
//         else if( freq_s[s[l]] > freq_t[s[l]]){
//             freq_s[s[l]] -= 1
//             l++;
//         }
//         else {
//             break
//         }
//     }
//     while(max_len >= l) {
//         if (!(s[max_len] in freq_t)){
//             max_len--;
//         }
//         else if( freq_s[s[max_len]] > freq_t[s[max_len]]){
//             freq_s[s[max_len]] -= 1
//             max_len--;
//         }
//         else {
//             break
//         }
//     }
//
//     console.log(l, max_len)
//     return s.substring(l,max_len+1)
// };

let minWindow = function (s, t) {
    // base case
    if (t.length > s.length) {
        return ""
    }

    let freqT = findFrequency(t);
    let freqW = {};
    let lengthT = t.length;

    let left = 0;
    let right = 0;
    let maxLen = 9999999999;
    let subStr = ""

    while (left <= right) {
        let char = s[right];
        if (char in freqT) {
            if (char in freqW) {
                freqW[char] += 1;
            } else {
                freqW[char] = 1;
            }

            if (freqW[char] <= freqT[char]) {
                lengthT -= 1;
            }
        }
        if (lengthT === 0 || right === s.length - 1) {
            if (lengthT === 0) {
                let len = right - left + 1;
                if (len < maxLen) {
                    maxLen = len;
                    subStr = s.substring(left, right + 1)
                }
            }

            let left_char = s[left];
            if (left_char in freqT) {
                freqW[left_char] -= 1;
                if (freqW[left_char] < freqT[left_char]) {
                    lengthT += 1;
                }
            }
            left++;
            while (left <= right && !(s[left] in freqT)) {
                left++;
            }
            if (char in freqT) {
                freqW[char] -= 1;
                if (freqW[char] < freqT[char]) {
                    lengthT += 1;
                }
            }
            right--;
        }

        if (right < s.length) {
            right++;
        }
    }
    return subStr;
}
// console.log(minWindow(s = "ADOBECODEBANC", t = "ABC"));
// console.log(minWindow( s = "a", t = "a"));
console.log(minWindow(s = "a", t = "aa"));
// console.log(minWindow(s = "ABEADBACNC", t = "ABCA"));
// console.log(minWindow(s = "cabwefgewcwaefgcf", t = "cae"));