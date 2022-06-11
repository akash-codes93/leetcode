/**
 * https://leetcode.com/problems/camelcase-matching/
 */

let eachCaseMatch = (query, pattern) => {
    let i = 0;
    let j = 0;
    while (i < query.length && j < pattern.length) {
        if (query[i] === pattern[j]) {
            i++;
            j++;
        } else {
            if (query.charCodeAt(i) <= 90 && query.charCodeAt(i) >= 65) {
                return false
            }
            i++;
        }
    }
    if (j !== pattern.length) {
        return false
    }

    while (i < query.length) {
        if (query.charCodeAt(i) <= 90 && query.charCodeAt(i) >= 65) {
            return false
        }
        i++;
    }
    return true
}


let camelMatch = (queries, pattern) => {
    let output = [];
    queries.forEach(query => {
        output.push(eachCaseMatch(query, pattern));
    })
    return output
};

o = camelMatch(["ForceFeedBack"], "FB")
console.log(o)