/*
https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/
 */

/**
 * task1: find len of ll
 * task2: find mid of ll
 * task3: reverse other mid of ll
 * task4: traverse two ll and find max
 * @param head
 */

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

let pairSum = function (head) {
    let ll_len = length(head);
    let mid = find_mid_start(head, ll_len);
    console.log(mid.val)
    mid = reverse(mid)
    let sum = 0;
    while(mid != null){
        let current_sum = mid.val + head.val
        if(current_sum > sum){
            sum = current_sum
        }
        mid = mid.next
        head = head.next
    }
    return sum
};

// 1->2->3->4