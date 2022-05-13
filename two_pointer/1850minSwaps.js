/*
https://leetcode.com/problems/minimum-adjacent-swaps-to-reach-the-kth-smallest-number/
 */
// this is not done
/**
 * copied to find the next permutation
 * @param array
 * @returns {boolean|*}
 */
function nextPermutation(array) {
    var i = array.length - 1;
    while (i > 0 && array[i - 1] >= array[i]) {
        i--;
    }

    if (i <= 0) {
        return false;
    }

    var j = array.length - 1;

    while (array[j] <= array[i - 1]) {
        j--;
    }

    var temp = array[i - 1];
    array[i - 1] = array[j];
    array[j] = temp;

    j = array.length - 1;

    while (i < j) {
        temp = array[i];
        array[i] = array[j];
        array[j] = temp;
        i++;
        j--;
    }

    return array;
}

let getMinSwaps = function (num, k) {
    let nums = num.split("")
    let original = num.split("")
    let res = 0
    while (k > 0) {
        nums = nextPermutation(nums)
        k--;
    }
    console.log(nums);
    console.log(original);
    for (let i = 0; i < original.length; i++) {
        if (original[i] === nums[i]) {
            continue
        }
        let j = i + 1;
        while(j < nums.length)  {
            console.log(j)
            if (original[i] === nums[j]) {
                console.log("matched")
                break
            }
            j++;
            console.log("after increment")
        }
        console.log(j, i)
        res = res + (j - i)
        let p = nums[i]
        nums[i] = nums[j]
        nums[j] = p
        console.log(nums)
    }

    return res
};

o = getMinSwaps("059", 5)
console.log(o)