/*
https://leetcode.com/problems/reverse-prefix-of-word/
 */

var reversePrefix = function (word, ch) {
    var word_array = word.split("")
    var first_index = -1

    for (let i = 0; i < word_array.length; i++) {
        if (word_array[i] === ch) {
            first_index = i
            break
        }
    }
    if (first_index === -1) {
        return word
    }
    var start =0
    var freeze = first_index
    while (start <= freeze / 2) {
        console.log(start, first_index)
        let p = word_array[start]
        word_array[start] = word_array[first_index]
        word_array[first_index] = p

        start++;
        first_index--;
    }

    return word_array.join("")

};

o = reversePrefix("arzquwnjyn", "j")
console.log(o)