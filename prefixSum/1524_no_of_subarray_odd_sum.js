/*
https://leetcode.com/problems/number-of-sub-arrays-with-odd-sum/
maintain a hash map with two keys odd, even
odd - odd = even
even - odd = odd
odd-even = odd
 */

var numOfSubarrays = function(arr) {
    let hash_map = {
        "even": 0,
        "odd": 0
    }

    let count = 0;
    let sum_till_now = 0;

    for(let i=0; i < arr.length; i++){
        sum_till_now += arr[i];

        if(sum_till_now % 2 !== 0){
            count += 1
            count += hash_map["even"]
            hash_map["odd"] += 1
        }
        else {
            count += hash_map["odd"]
            hash_map["even"] += 1
        }
    }
    return count % (10**9 + 7)
};

console.log(numOfSubarrays([1,3,5]))
console.log(numOfSubarrays([2,4,6]))
console.log(numOfSubarrays([1,2,3,4,5,6,7]))
