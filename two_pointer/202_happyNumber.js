/**
 * https://leetcode.com/problems/happy-number/
 */
let sum_of_square_of_digits = (n) => {
    let p = n;
    let sum = 0;

    while (p !== 0) {
        let last = (p % 10);
        sum += last * last
        p = parseInt(p / 10)
    }
    return sum
}


let isHappy = function (n) {
    let distinct_sum = new Set();

    while (true) {
        let sum_digits = sum_of_square_of_digits(n)
        if (sum_digits === 1) {
            return true
        }
        if (distinct_sum.has(sum_digits)) {
            return false
        } else {
            distinct_sum.add(sum_digits)
            n = sum_digits
        }
    }
};

o = isHappy(2)
console.log(o)
