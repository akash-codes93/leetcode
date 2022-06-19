/**
 * https://leetcode.com/problems/backspace-string-compare/
 */


let safeString = (s) => {
    let remaining_s = [];
    let i = s.length - 1;
    let hash_count = 0;
    while (i >= 0) {
        if (s[i] === "#") {
            hash_count++;
        } else if (s[i] !== "#" && hash_count !== 0) {
            hash_count--;
        } else {
            remaining_s.push(s[i]);
        }
        i--;
    }

    return remaining_s;
}

/**
 * using auxiliary arrays
 * time: O(n)
 * space: O(n)
 * @param s
 * @param t
 * @returns {boolean}
 */

let backspaceCompare1 = (s, t) => {

    let remaining_s = safeString(s);
    let remaining_t = safeString(t);
    // console.log(remaining_s, remaining_t)
    let i = remaining_s.length;
    let j = remaining_t.length;

    while (i >= 0 && j >= 0) {
        if (remaining_s[i] !== remaining_t[j]) {
            return false
        }
        i--;
        j--;
    }
    // console.log(i, j)
    if (i < 0 && j < 0) {
        return true
    }
    return false;
};

/**
 * two pointer very simple logic
 * time: O(n)
 * space: O(1)
 * lot of condition because edge cases were failing
 * rough idea is as you encounter hash start a separate for loop to remove characters
 * not easy for sure
 */

let backspaceCompare = (s, t) => {
    let i = s.length;
    let j = t.length;

    while (i >= 0 && j >= 0) {
        i--;
        j--;

        if (s[i] === "#") {
            let hash_count = 1;
            i = i - 1
            while ((hash_count !== 0 || s[i] === "#") && i >=0) {
                if (s[i] === "#") {
                    hash_count++;
                } else {
                    hash_count--;
                }
                i--;
            }
        }

        if (t[j] === "#") {
            let hash_count = 1;
            j = j - 1
            while ((hash_count !== 0 || t[j] === "#") && j >= 0) {
                if (t[j] === "#") {
                    hash_count++;
                } else {
                    hash_count--;
                }
                j--;
            }
        }

        if (s[i] !== t[j]) {
            return false
        }

    }

    if (i < 0 && j < 0) {
        return true
    }
    return false;

}

// o = backspaceCompare(s = "ab#c", t = "ad#c")
// o = backspaceCompare(s = "ab##", t = "c#d#")
// o = backspaceCompare(s = "a#c", t = "bc")
// o = backspaceCompare("xywrrmp","xywrrmu#p")
// o = backspaceCompare("bxj##tw", "bxj###tw")

console.log(o)

