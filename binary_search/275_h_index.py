
class Solution:
    def hIndex(self, arr) -> int:

        h_index = 0
        l = 0
        r = len(arr) - 1

        while l <= r:
            mid = l + (r - l) // 2
            z = len(arr) - mid

            if arr[mid] - z < 0:
                l = mid + 1

            elif arr[mid] - z >= 0:
                r = mid - 1

                if h_index < z:
                    h_index = z

        return h_index


"""

[[1,1],2,[1,1]]
[1,[4,[6]]]


"""