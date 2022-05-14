/*
https://leetcode.com/problems/rotating-the-box/
 */

let rotateArray = (box) => {
    let count = 0
    let start = box.length - 1;
    let count_array = new Array(box.length).fill(0);
    while (start >= 0) {
        if (box[start] === '.') {
            count++;
        } else if (box[start] === '*') {
            count = 0;
        }
        count_array[start] = count;
        start--;
    }

    // console.log(count_array);
    start = box.length - 2;
    while (start >= 0) {
        if (box[start] === '#') {
            box[start] = '.'
            box[start + count_array[start]] = '#'
        }
        start--;
    }
    return box
}


let transformArray = function (box) {
    let rot = new Array(box[0].length)
    for (let i = 0; i < box[0].length; i++) {
        rot[i] = new Array(box.length)
    }
    for (let i = 0; i < rot.length; i++)
        for (let j = 0; j < rot[i].length; j++)
            rot[i][j] = box[rot[i].length - j - 1][i]
    return rot
}

let rotateTheBox = function (box) {
    for (let i = 0; i < box.length; i++) {
        box[i] = rotateArray(box[i])
    }
    box = transformArray(box)
    return box
};

// o = rotateTheBox(["#",".","#"])
// o = rotateTheBox(["#", ".", "*", "#", ".", ".", "#", "#", '.'])
// o = rotateTheBox([["#", ".", "*", "."]])
o = rotateTheBox([["#", ".", "*", "."],
    ["#", "#", "*", "."]])
console.log(o)
