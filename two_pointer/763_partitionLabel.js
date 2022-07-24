/*
https://leetcode.com/problems/partition-labels/
 */

var partitionLabels = function (s) {
    var dict = {}

    for (let i = 0; i < s.length; i++) {
        var letter = s[i]
        if (letter in dict) {
            var value = dict[letter]
            if (i > value) {
                dict[letter] = i
            }
        } else {
            dict[letter] = i
        }
    }
    var output = []
    var size = 0
    var end = 0
    for (let i = 0; i < s.length; i++){
        let last_index = dict[s[i]]
        if (i > end) {
            output.push(size);
            size = 1;
            end = last_index
        }
        else if(last_index > end) {
            end = last_index
            size = size + 1
        }
        else{
            size = size +1
        }
    }
    output.push(size)
    return output

}

o = partitionLabels("ababcbacadefegdehijhklij")
o = partitionLabels("eccbbbbdec")
console.log(o)