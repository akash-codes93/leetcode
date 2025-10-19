"""
Minimum swaps required to sort and array
Given: 
    all elements in the array are distinct
    len(arr) <= 10^5

cycle detection question
"""

class Solution:
    
    #Function to find the minimum number of swaps required to sort the array.
    def minSwaps(self, arr):
		#Code here
        n = len(arr)
        temp = sorted(arr)
        pos = {}
        total_swaps = 0

        for i in range(n):
            pos[temp[i]] = i

        vis = [False] * n

        for i in range(n):

            if vis[i] and pos[arr[i]] == i:
                continue
            cycle_size = 0
            j = i

            while vis[j] != True:

                vis[j] = True

                correct_pos = pos[arr[j]]
                cycle_size += 1

                j = correct_pos 

            if cycle_size > 0:
                total_swaps += (cycle_size - 1)
        
        return total_swaps


                











		






