/**
 * https://leetcode.com/problems/find-a-peak-element-ii/

 * ::: Not Solved :::
 */

let checkingUndefined = (val) => {
    if (val === undefined){
        return -1
    }
    else {
        return val
    }
}

let findPeakGrid = function (mat) {
    // base case
    if (mat.length === 1 && mat[0].length === 1) {
        return [0, 0]
    }
    /**
    for (let i = 0; i < mat.length; i++) {

        let arr = mat[i]
        let l = 0;
        let r = mat[0].length - 1;
        let mid = -1;

        while (l <= r) {
            mid = Math.floor((l + r) / 2);
            let j = mid;

            let mid_value = arr[mid]

            let up = checkingUndefined(mat[i - 1][j])
            let down = checkingUndefined(mat[i + 1][j])
            let left = checkingUndefined(mat[i][j - 1])
            let right = checkingUndefined(mat[i][j + 1])

            if (mid_value > up && mid_value > down && mid_value > left && mid_value > right){
                return [i, mid]
            } else if () {

            }


        }

    }
     **/


};