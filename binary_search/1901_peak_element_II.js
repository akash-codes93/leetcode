/**
 * https://leetcode.com/problems/find-a-peak-element-ii/
 * @param {number[][]} mat
 * @return {number[]}
 * ::: Not Solved :::
 */

var findPeakGrid = function (mat) {
    // base case
    if (mat.length === 1 && mat[0].length === 1) {
        return [0, 0]
    }

    for (let i = 0; i < mat.length; i++) {

        let arr = mat[i]
        let l = 0;
        let r = mat[0].length - 1;
        let mid = -1;

        while (l <= r){
            mid = Math.floor((l+r)/2);

            let mid_value = arr[mid]

            pass


        }

    }
};