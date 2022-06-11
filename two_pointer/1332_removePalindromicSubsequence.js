/**
 * https://leetcode.com/problems/remove-palindromic-subsequences/
 * its a subsequence not a substring that means not continuous
 * since there are only a and b
 * so answer will either 0 1 or 2
 */

let checkPalindrome = (string) => {

    const len = string.length;

    for (let i = 0; i < len / 2; i++) {
        if (string[i] !== string[len - 1 - i]) {
            return false;
        }
    }
    return true;
}

let removePalindromeSub = (s) => {
    if(s == ""){
        return 0
    }
    else if(checkPalindrome(s)){
        return 1
    }
    else{
        return 2
    }
};

// o = removePalindromeSub("ababa")
o = removePalindromeSub("bbaabaaa")
console.log(o);
