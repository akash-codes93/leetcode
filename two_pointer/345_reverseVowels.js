/**
 * https://leetcode.com/problems/reverse-vowels-of-a-string/
 */

let reverseVowels = s => {

    s = s.split("")
    let vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'];
    let l = 0;
    let r = s.length - 1;

    while(l < r){
        if (vowel.indexOf(s[l]) !== -1 &&  vowel.indexOf(s[r]) !== -1 ){
            let k = s[l];
            s[l] = s[r];
            s[r] = k;
            l++;
            r--;
        }
        else if(vowel.indexOf(s[l]) === -1){
            l++;
        }
        else if(vowel.indexOf(s[r]) === -1){
            r--;
        }
    }
    return s.join("")
};

o = reverseVowels("aA")
console.log(o)
