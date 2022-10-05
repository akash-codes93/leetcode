/**
 * https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/
 * Binary search not on array but on min and max elems on array
 *
 * Hints:
 *  - if on x day we can make t boq.
 *
 *  Time: O(nlog(n)) // not because of sorting but we do binary search on min and max elem and for every (min + max)/2 we traverse the array
 *  log(n) * n
 *  Space: O(1)
 */

let boqInDays = (bloomDay, mid, k) => {

    let noOfBoq = 0;
    let flowers = 0;

    for (let i = 0; i < bloomDay.length; i++) {
        if (bloomDay[i] <= mid) {
            flowers++;
        } else {
            flowers = 0;
        }

        if (flowers === k) {
            noOfBoq++;
            flowers = 0
        }
    }
    return noOfBoq;
}

let minDays = function (bloomDay, m, k) {

    //base case
    if ((m * k) > bloomDay.length) {
        return -1;
    }

    // equality case
    if ((m * k) === bloomDay.length) {
        bloomDay.sort((a, b) => (a - b));
        return bloomDay[bloomDay.length - 1];
    }

    let l = Math.min(...bloomDay);
    let r = Math.max(...bloomDay);
    let res = 0;

    while (l <= r) {
        let mid = Math.floor((l + r) / 2);

        let noOfBoq = boqInDays(bloomDay, mid, k);

        if (noOfBoq >= m) {
            res = mid;
            r = mid - 1
        } else {
            l = mid + 1
        }

    }

    return res;
};
// checking boqInDays function
// console.log(boqInDays([1, 10, 3, 8, 2, 6], 8, 2))


// console.log(minDays([1, 10, 3, 8, 2, 6], 2, 3))
console.log(minDays([7,7,7,7,12,7,7], 2, 3))

