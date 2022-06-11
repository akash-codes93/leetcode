/**
 * https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
 */

let twoSum = (numbers, target) => {

    let i = 0;
    let j = numbers.length - 1;

    while (i < j) {
        if (numbers[i] + numbers[j] > target){
            j--;
        }
        else if (numbers[i] + numbers[j] < target){
            i++;
        }
        else{
            return [i+1, j+1]
        }
    }

};

// o = twoSum(numbers = [2,7,11,15], target = 9)
o = twoSum(numbers = [-1,0], target = -1)
console.log(o)