/**
 * https://leetcode.com/problems/remove-nth-node-from-end-of-list/
 */

const {ListNode, printLinkedList} = require('./base')


let removeNthFromEnd = function (head, n) {
    let traverse = head;
    let len = 0;
    while (traverse != null) {
        len++;
        traverse = traverse.next
    }

    traverse = head;
    let nodeToRemove = len - n + 1;

    if (nodeToRemove === 1){
        head = head.next
    }
    else {
        nodeToRemove--;
        while (nodeToRemove !== 1) {
            nodeToRemove--;
            traverse = traverse.next;
        }

        if (traverse.next === null) {
            traverse.next = null
        } else {
            traverse.next = traverse.next.next;
        }
    }

    return head;
};




node5 = new ListNode(5)
node4 = new ListNode(4, node5)
node3 = new ListNode(3, node4)
node2 = new ListNode(2, node3)
head = new ListNode(1, node2)

printLinkedList(head)
head = removeNthFromEnd(head, 5)
printLinkedList(head)


