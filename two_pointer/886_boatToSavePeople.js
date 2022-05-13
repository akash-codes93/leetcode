/*
https://leetcode.com/problems/boats-to-save-people/
 */

var numRescueBoats = function (people, limit) {

    people.sort()
    people.sort(function(a, b) {
        return a - b;
    });
    let trips = 0
    let left = 0
    let right = people.length - 1;

    while (left <= right) {
        if (right === left) {
            trips = trips + 1
            left = left + 1
            right = right - 1
        }
        else if (people[left] + people[right] > limit) {
            trips = trips + 1
            right = right - 1
        }
        else {
            trips += 1
            left = left + 1
            right = right - 1
        }
    }

    return trips;
};

trips = numRescueBoats([44,10,29,12,49,41,23,5,17,26], 50)
console.log(trips)