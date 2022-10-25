/**
 * https://leetcode.com/problems/partition-list/
 * :: linked list
 */

const {printLinkedList, linkedListFromArray} = require('./base')

let partition = (head, x) => {

    if (head == null) {
        return null;
    }

    let tr = head;
    let prev = null;

    while (tr != null && tr.val < x) {
        prev = tr;
        tr = tr.next;
    }

    // console.log(tr.val);
    // console.log(prev.val);

    let tr_other = tr
    let prev_new = prev;
    while (tr_other !== null) {
        if (tr_other.val < x) {
            let p = tr_other.next;
            prev_new.next = tr_other.next;
            if (prev === null) {
                tr_other.next = head;
                head = tr_other
            } else {
                tr_other.next = prev.next;
                prev.next = tr_other;
            }

            // console.log("----")
            // console.log(tr_other.val);
            // console.log(prev.val);
            // console.log("----")
            prev = tr_other;
            tr_other = p;
        } else {
            prev_new = tr_other;
            tr_other = tr_other.next
        }

    }
    return head
};


l1 = linkedListFromArray([4,3,2,5,2])
l2 = partition(l1, 3)
printLinkedList(l2)
