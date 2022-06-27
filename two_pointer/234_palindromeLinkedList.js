/**
 * https://leetcode.com/problems/palindrome-linked-list/
 */

/**
 * 1 > 2 > 2 > 1
 * 1 > 2 > 1 > 2
 * @param head
 */

/**
 * Definition for singly-linked list.

 */

function ListNode(val, next) {
    this.val = (val===undefined ? 0 : val)
    this.next = (next===undefined ? null : next)
}


let length = function (head) {
    let total = 0;
    let start = head;
    while (start != null) {
        total++;
        start = start.next;
    }
    return total
}

let find_mid_start = function(head, total) {
    let mid = 0;
    let start = head;
    while(mid < total/2){
        start = start.next
        mid = mid + 1;
    }
    return start
}


let reverse = function (head){
    let previous = null;
    let current = head;

    while(current != null){
        let p = current.next
        current.next = previous

        previous = current
        current = p;
    }

    return previous
}


let isPalindrome = function(head) {

    if(head.next === null){
        return true
    }

    let ll_len = length(head);
    let mid = find_mid_start(head, ll_len);
    mid = reverse(mid)
    let check = mid

    while(head != check){
        if(head.val != mid.val){
            return false
        }
        head = head.next;
        mid = mid.next
    }
    return true
};

l2 = new ListNode(6)
l1 = new ListNode(6, l2)

isPalindrome(l1)