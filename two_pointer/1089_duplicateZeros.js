/**
 * https://leetcode.com/problems/duplicate-zeros/
 */

/**
 * used queue
 * time: O(n)
 * space: O(n)
 * @param arr
 * @returns {*}
 */
let duplicateZeros1 = function (arr) {

    let i = 0;
    let shift_value = [];
    let shift = 0

    while (i < arr.length) {
        if (shift !== 0 && arr[i] === 0) {
            shift_value.push(0);
            shift_value.push(0);
            arr[i] = shift_value.shift()
            i = i + 1
            shift += 1
        } else if (shift === 0 && arr[i] === 0) {
            shift_value.push(arr[i])
            shift += 1
            i++;
        } else if (shift === 0) {
            i++;
        } else {
            shift_value.push(arr[i])
            arr[i] = shift_value.shift()
            i++;
        }
    }
    return arr
};


/**
 * two pointer
 * add extra zeros to array and then do two pointer swap
 * time: O(n)
 * space: O(1)
 * @param arr
 */

let countZeros = (arr) => {
    let count = 0;
    for (let i = 0; i < arr.length; i++) {
        if (arr[i] === 0) {
            count++;
        }
    }
    return count;
}

let duplicateZeros = function (arr) {
    let zeros = countZeros(arr);
    let i = arr.length - 1;
    let j = arr.length + zeros - 1;

    while (i < j) {
        if(j < arr.length){
            arr[j] = arr[i]
        }
        if(arr[i] === 0){
            j = j-1
            if(j< arr.length){
                arr[j] = arr[i]
            }
        }
        i -= 1
        j -= 1
    }
}


o = duplicateZeros([1, 0, 2, 3, 0, 4, 5, 0, 1, 2])
// o = duplicateZeros([1, 2, 3])
console.log(o)

