/**
 * https://leetcode.com/problems/merge-two-sorted-lists/
 */

const {ListNode, printLinkedList, goToNextNode, linkedListFromArray} = require('./base')

let compareValue = (node1, node2) => {
    let node1Value = 9999999
    let node2Value = 9999999
    if (node1 !== null) {
        node1Value = node1.val
    }
    if (node2 !== null) {
        node2Value = node2.val
    }

    return node1Value <= node2Value;

}


let mergeTwoLists = function (list1, list2) {
    let traverse1 = list1;
    let traverse2 = list2;
    let traverse = null;
    let head = null;

    if (compareValue(traverse1, traverse2)) {
        traverse = traverse1;
        traverse1 = goToNextNode(traverse1);
    } else {
        traverse = traverse2;
        traverse2 = goToNextNode(traverse2);
    }
    head = traverse;

    while (traverse1 !== null || traverse2 !== null) {
        if (compareValue(traverse1, traverse2)) {
            traverse.next = traverse1;
            traverse1 = goToNextNode(traverse1);
        } else {
            traverse.next = traverse2;
            traverse2 = goToNextNode(traverse2);
        }
        traverse = traverse.next;
    }

    return head;

};


// list1 = linkedListFromArray([1,2,4])
// list1 = linkedListFromArray([])
// list1 = linkedListFromArray([])
list1 = linkedListFromArray([1,3])
printLinkedList(list1);
// list2 = linkedListFromArray([1,3,4])
// list2 = linkedListFromArray([])
// list2 = linkedListFromArray([0])
list2 = linkedListFromArray([2])
printLinkedList(list2);
head = mergeTwoLists(list1, list2);
printLinkedList(head);
