/**
 * https://leetcode.com/problems/minimum-garden-perimeter-to-collect-enough-apples/
 *
 * A(L) = A(L-1) + for(L->L/2) [L*4] + [L/2*4] + Rest multiply by 8
 * where L is even
 * Update :: the above approach is not optimised
 * Not solved
 */


let minimumPerimeter = function (neededApples) {
    // Time: O(N)
    let total_apples = 0;
    let i = 0
    while (total_apples < neededApples) {
        i = i + 2;
        // the below loop can be skipped. need to figure-out the formula
        for (let p = i; p >= i / 2; p--) {
            if (p === i || p === i / 2) {
                total_apples += p * 4
            } else {
                total_apples += p * 8
            }
        }
    }

    return i
};

// console.log(minimumPerimeter(12))
// console.log(minimumPerimeter(60))
console.log(minimumPerimeter(150))
// console.log(minimumPerimeter(400))
// console.log(minimumPerimeter(462332582464270))