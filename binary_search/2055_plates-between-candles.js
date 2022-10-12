/**
 * https://leetcode.com/problems/plates-between-candles/
 * Idea is simple
 * * - 0
 * | - 1
 * [0, 1, 0,1 ,0]
 * create a sum array
 * [0,1,1,2,2]
 * apply binary search to find the right and left(little tricky) most bar in the given a, b
 */

let platesBetweenCandles = function (p, queries) {
    let s = p.split('')

    for (let i = 0; i < s.length; i++) {
        if (s[i] === '*') {
            s[i] = 0;
        } else {
            s[i] = 1;
        }
    }
    let sum_tot = 0;
    for (let i = 0; i < s.length; i++) {
        sum_tot += s[i]
        s[i] = sum_tot
    }
    let output = []
    for (let i = 0; i < queries.length; i++) {
        let l = queries[i][0];
        let r = queries[i][1];
        let mid = 0;
        let l_mid = 0;
        let r_mid = 0;

        while (l <= r) {
            mid = Math.floor((l + r) / 2)
            if (s[r] > s[mid]) {
                l = mid + 1;
            } else if (r === l) {
                break
            } else {
                r = mid;
            }
        }
        r_mid = mid;
        l = queries[i][0];
        let find_val = s[l]
        if (p[l] === '*') {
            find_val = find_val + 1
        }
        r = r_mid;

        while (l <= r) {
            mid = Math.floor((l + r) / 2)
            if (find_val < s[mid]) {
                r = mid - 1;
            } else if (find_val === s[mid]){
                r = mid
            }
            else if(s[mid] < find_val){
                l = mid+1
            }

            if (l === r){
                break
            }

        }
        l_mid = mid;
        console.log(l_mid, r_mid)
        output.push((r_mid - l_mid - 1) - (s[r_mid] - s[l_mid] - 1))

    }

    return output
};


// console.log(platesBetweenCandles("**|**|***|", [[2, 5]]))
// console.log(platesBetweenCandles("***|**|*****|**||**|*", [[4, 17]]))
console.log(platesBetweenCandles("**|*******************|**********************************************|************|*********|*****|*********************************************************************************************|***",
    [[31, 96]]))

