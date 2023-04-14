/**
 * https://leetcode.com/problems/sqrtx/
 */

//let mySqrt = function (x) {
//    let l = 0;
//    let r = x / 2;
//
//    // base case
//    if(x === 1){
//        return 1
//    }
//
//    while (l <= r) {
//        let mid = (l + r) / 2
//        console.log(mid)
//
//        if ((Math.floor(r) - Math.floor(l)) < 1) {
//            return Math.floor(mid);
//        }
//
//        if (mid * mid < x) {
//            l = mid;
//        } else if (mid * mid === x) {
//            return mid
//
//        } else {
//            r = mid;
//        }
//
//    }
//};

let mySqrt = function (x) {
    let l = 0;
    let r = Math.floor(x/2);

    // base case
    if(x === 1) {
        return 1;
    }

    let mid = -1;

    while (l <= r) {
        mid = Math.floor( (l + r)/2);

        if (mid*mid == x){
            return mid;

        }
        else if (mid*mid < x){
            l = mid + 1;

        }
        else {
            r = mid-1
        }
    }

//    console.log("Not found in while loop for " + x);
//    console.log(l, mid, r);
    return Math.min(l, r)

}

console.log(mySqrt(9))
console.log(mySqrt(8))
console.log(mySqrt(7))
console.log(mySqrt(6))
console.log(mySqrt(10))
console.log(mySqrt(19))
console.log(mySqrt(4))