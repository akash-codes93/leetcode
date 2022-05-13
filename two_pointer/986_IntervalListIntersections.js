/*
https://leetcode.com/problems/interval-list-intersections/
 */
let intervalIntersection = function(firstList, secondList) {

    let end = 1
    let start = 0

    let first = 0
    let second = 0
    let final = [];

    while(first < firstList.length && second < secondList.length){

        if(firstList[first][end] >= secondList[second][start] && firstList[first][start] <= secondList[second][end]){
            final.push([
                Math.max(firstList[first][start], secondList[second][start]),
                Math.min(firstList[first][end], secondList[second][end]),
            ])
        }
        if (firstList[first][end] < secondList[second][end]){
            first += 1
        }
        else{
            second += 1
        }

    }
    return final;
};
// o = intervalIntersection([[0,2],[5,10],[13,23],[24,25]], [[1,5],[8,12],[15,24],[25,26]])
o = intervalIntersection([[1,3],[5,9]], [[2, 7]])
console.log(o)