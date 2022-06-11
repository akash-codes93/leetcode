/**
 * https://leetcode.com/problems/two-sum-iv-input-is-a-bst/
 */

let findTargetNode = (current, root, k) => {

    if (current == null) {
        return false
    }

    let find = 0;
    let remaining = k - root.val;
    let sub = root;

    while (sub !== null && find === 0) {
        if (sub === current) {
            sub = sub.left
        } else if (sub.val + current.val < k) {
            sub = sub.right;
        } else if (sub.val + current.val > k) {
            sub = sub.left
        } else {
            find = 1;
        }
    }

    if (find === 1) {
        return true
    } else {
        return findTargetNode(current.left, root, k) || findTargetNode(current.right, root, k)
    }
}

let findTarget = (root, k) => {

    return findTargetNode(root, root, k)

};

/*
[2,1,3]
4
 */