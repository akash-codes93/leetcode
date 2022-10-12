/**
 *
 * https://leetcode.com/problems/reach-a-number/
 * approach
 *  keep on adding numbers from 1 to n
 *  till n exceeds target
 *
 *  case 1 if target - sum(n) is even then answer is sum
 *  example: target is 11
 *  then 1+2+3+4+5= 15
 *  15 - 11 i= 4
 *  for if we remove 4/2 =2 to negative then problem solved
 *
 *  case 2 target - sum(n) is odd ans is n+2
 *
 */


let reachNumberRec = function (target, total, move) {
    // Good thinking but too many recursion in case of 1000000000
    if (total === target ) {
        return move
    }

    if (Math.abs(total) > Math.abs(target)) {
        return 999999999
    }

    move++;

    return Math.min(reachNumberRec(target, total + move, move), reachNumberRec(target, total - move, move))

};

let reachNumber = function (target) {

    // return reachNumberRec(Math.abs(target), 0, 0)
    target = Math.abs(target)
    let sum_tot = 0;
    for(let i =0; i<100000000000; i++){
        sum_tot += i;
        if(sum_tot >= target){
            if((sum_tot - target)%2 === 0) {
                return i
            }
        }
    }
}

// console.log(reachNumber(2, 0, 0))
// console.log(reachNumber(3, 0, 0))
// console.log(reachNumber(-1, 0, 0))
// console.log(reachNumber(-1000000000, 0, 0))
// console.log(reachNumber(4, 0, 0))
console.log(reachNumber(5, 0, 0))
// console.log(reachNumber(6, 0, 0))
// console.log(reachNumber(7, 0, 0))
// console.log(reachNumber(8, 0, 0))