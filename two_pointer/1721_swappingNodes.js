/*
https://leetcode.com/problems/swapping-nodes-in-a-linked-list/
 */

let length = head => {
    let total = 0;
    let start = head;
    while (start != null) {
        total++;
        start = start.next;
    }
    return total
}

let find_node_at_index = (head, k) => {
    let start = head;
    while(k-1 > 0){
        start = start.next
        k--
    }
    return start
}


let swapNodes = function(head, k) {
    let len = length(head)
    let node_at_index_first = find_node_at_index(head, k)
    let node_at_index_last = find_node_at_index(head, (len- k +1))
    let p = node_at_index_first.val
    node_at_index_first.val = node_at_index_last.val
    node_at_index_last.val = p
};