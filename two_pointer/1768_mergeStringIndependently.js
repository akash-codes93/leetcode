/**
 * https://leetcode.com/problems/merge-strings-alternately/
 */


let mergeAlternately = function (word1, word2) {
    let word1_len = word1.length;
    let word2_len = word2.length;

    let greater = word1_len;
    if (word2_len > greater) {
        greater = word2_len;
    }
    let word3 = []
    let word1_i = 0;
    let word2_i = 0;

    for (let i = 0; i < greater; i++) {
        if (word1_i < word1_len){
            word3.push(word1[word1_i])
            word1_i++;
        }
        if (word2_i < word2_len){
            word3.push(word2[word2_i])
            word2_i++;
        }
    }
    return word3.join("")
};

let o = mergeAlternately("ab",  "pqrs")
console.log(o)