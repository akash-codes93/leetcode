/**
 * https://leetcode.com/problems/swap-nodes-in-pairs/
 * BETTER: instead of pairs solve for general value
 *
 */

const {printLinkedList, linkedListFromArray} = require('./base')


let reverseNodeBetweenStartEnd = (start, end) => {
    let tr = start;
    let previous = null;
    while (true) {
        let p = tr.next;
        tr.next = previous;

        previous = tr;

        if (tr === end) {
            break;
        }
        tr = p;
    }
}


let swapPairs = function (head, k) {
    let traverse = head;
    let count = 0;
    let start = null;
    let new_head = head;
    let previous_start = null;
    let new_head_set = false;

    while (traverse !== null) {
        count++;

        if (count === 1) {
            start = traverse
        }

        if (count === k) {
           let start_next = traverse.next;
            reverseNodeBetweenStartEnd(start, traverse)
            if(previous_start !== null) {
                previous_start.next = traverse;
            }

            if (new_head_set === false) {
                new_head = traverse;
                new_head_set = true;
            }
            start.next = start_next
            previous_start = start;
            traverse = start_next;
            count = 0;
        } else {
            traverse = traverse.next;
        }

    }
    return new_head
};

l1 = linkedListFromArray([1,2,3,4])
l2 = swapPairs(l1, 3)
printLinkedList(l2)