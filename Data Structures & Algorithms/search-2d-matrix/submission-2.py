class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # first looking at our constraints
        # we know that the array/subarrays have to be at least of length 1, so we can build test cases around this
       
        # our naive/suboptimal approach would be to iterate through all elements searching for our target
        # but this solution is O(n^2)

        # we know that the matrix is sorting in increasing order, so this makes it very easy to search
        # for our target using a binary search

        # first, lets define m and n of the matrix
        m = len(matrix)
        n = len(matrix[0])

        # now, lets instantiate our left and right pointers for our binary search
        left, right = 0, (m*n)-1

        # now lets run our binary search
        while left <= right:
            # we can calculate the current mid using our left and right pointers
            mid = left + (right - left) // 2

            # now, we do face an issue, and that is that the current indicies we have only works on a
            # flattened array. to fix this, we have to convert our indicies to a coordinate in the matrix
           
            # first, lets find our first dimension, which is our row
            midRow = mid // n
           
            # now lets calculate our second dimension conversion, which is our column
            midCol = mid % n

            # with these conversions, we can now run a basic binary search
            # if our left is smaller than target, we have to move it closer to mid
            if matrix[midRow][midCol] == target:
                return True
           
            elif matrix[midRow][midCol] < target:
                left = mid + 1
           
            # if not, then our right needs to move because it is too large compared to our midpoint
            else:
                right = mid - 1

        return False