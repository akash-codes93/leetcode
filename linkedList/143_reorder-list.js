/**
 * https://leetcode.com/problems/reorder-list/
 */
const {ListNode, printLinkedList, goToNextNode, linkedListFromArray} = require('./base')


let reorderList = function (head) {

    if (head == null) {
        return null;
    } else if (head.next == null) {
        return head
    }


    let tr_fast = head;
    let tr = head;

    while (tr_fast.next != null || tr_fast != null) {
        tr = tr.next;
        tr_fast = tr_fast.next.next;
        console.log(tr_fast);

    }
    console.log(tr);

};

l1 = linkedListFromArray([1, 2, 3, 4, 5])
reorderList(l1);
l2 = linkedListFromArray([1, 2, 3, 4, 5, 6])
reorderList(l2);

