class ListNode {
    constructor(val, next) {
        this.val = (val === undefined ? 0 : val)
        this.next = (next === undefined ? null : next)
    }
}

let printLinkedList = (head) => {
    console.log("========== Linked List ==========")
    while (head != null) {
        console.log(head.val)
        head = head.next
    }
    console.log("==========     End     ==========")
}

let goToNextNode = node => {
    if (node === null) {
        return node;
    }
    return node.next;
}

let linkedListFromArray = arr => {
    // edge case
    if (arr.length === 0) {
        return null
    }
    arr = arr.reverse();
    let prev = 0;
    for (let i = 0; i < arr.length; i++) {
        let node = null;
        if (i === 0) {
            node = new ListNode(arr[i]);
        } else {
            node = new ListNode(arr[i], prev)
        }
        prev = node;
    }
    return prev
}


module.exports = {
    ListNode: ListNode,
    printLinkedList: printLinkedList,
    goToNextNode: goToNextNode,
    linkedListFromArray: linkedListFromArray,
}

// head = linkedListFromArray([1, 2, 3, 4])
// printLinkedList(head);