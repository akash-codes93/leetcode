/*
https://leetcode.com/problems/pancake-sorting/
 */


let find_element = (nums, target) => {
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] === target) {
            return i
        }
    }
    return -1;
}

let flip = (nums, k) => {
    let start = 0;
    let end = k - 1
    while (start < end) {
        let p = nums[start]
        nums[start] = nums[end];
        nums[end] = p
        start++;
        end--;
    }
    return nums;
}


let pancakeSort = function (arr) {
    let last = arr.length;
    let flips = []
    while(last > 0){
        let last_index = find_element(arr, last);
        console.log(last_index)
        if(last_index === last){
            last--;
            continue
        }
        arr = flip(arr, last_index+1)
        console.log(arr)
        arr = flip(arr, last)
        console.log(arr)
        flips.push(last_index+1)
        flips.push(last)
        last --;
    }
    console.log(arr)
    return flips
};

o = pancakeSort([3,2,4,1])
console.log(o)