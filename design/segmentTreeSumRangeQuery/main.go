package main

import (
	"fmt"
	"math"
)

type segmentTree struct {
	st []int
}

type NumArray struct {
	nums  []int
	segTr segmentTree
}

func Constructor(nums []int) NumArray {
	n := len(nums)

	height := math.Ceil(math.Log2(float64(n + 1)))

	// Maximum size of segment tree
	max_size := int(2 * (math.Pow(2, height) - 1))

	st := make([]int, max_size)

	segTr := segmentTree{st}

	// constructing segment tree
	segTr.constructSegmentTree(0, nums, 0, len(nums)-1)

	numarray := NumArray{nums, segTr}

	return numarray

}

func (segTr segmentTree) constructSegmentTree(si int, nums []int, l int, r int) int {
	if l == r {
		segTr.st[si] = nums[l]
		return nums[l]
	}

	mid := int((l + r) / 2)

	segTr.st[si] = segTr.constructSegmentTree(2*si+1, nums, l, mid) + segTr.constructSegmentTree(2*si+2, nums, mid+1, r)

	return segTr.st[si]

}

func (segTr segmentTree) updateSegmentTree(si int, sl int, sr int, nums []int, val int, pos int) int {
	fmt.Println(si, sl, sr, nums, val, pos)
	if pos < sl || pos > sr {
		return segTr.st[si]
	}

	// leaf node
	if sl == sr {
		segTr.st[si] = val
		return val
	}

	// recreating sum
	mid := int((sl + sr) / 2)

	segTr.st[si] = segTr.updateSegmentTree(2*si+1, sl, mid, nums, val, pos) + segTr.updateSegmentTree(2*si+2, mid+1, sr, nums, val, pos)

	return segTr.st[si]

}

func (segTr segmentTree) sumRange(si int, sl int, sr int, nums []int, l int, r int) int {
	// no overlap
	if sr < l || sl > r {
		return 0
	}

	// total overlap
	if sl >= l && sr <= r {
		return segTr.st[si]
	}

	// partial overlap
	mid := int((sl + sr) / 2)
	return segTr.sumRange(2*si+1, sl, mid, nums, l, r) + segTr.sumRange(2*si+2, mid+1, sr, nums, l, r)

}

func (this *NumArray) Update(index int, val int) {
	this.nums[index] = val
	fmt.Println("upd range: ", this.nums, this.segTr.st)
	this.segTr.updateSegmentTree(0, 0, len(this.nums)-1, this.nums, val, index)
	fmt.Println("after upd: ", this.segTr.st)

}

func (this *NumArray) SumRange(left int, right int) int {
	fmt.Println("sum range: ", this.nums, this.segTr.st)
	return this.segTr.sumRange(0, 0, len(this.nums)-1, this.nums, left, right)

}

func main() {
	// nums := []int{1, 3, 5}

	nums := []int{9, -8}

	obj := Constructor(nums)
	obj.Update(0, 3)
	param_2 := obj.SumRange(1, 1)
	fmt.Println(param_2)
	param_2 = obj.SumRange(0, 1)
	fmt.Println(param_2)

}
