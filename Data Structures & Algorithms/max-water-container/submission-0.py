class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # essentially what we want to do is maximize both bounds,
        # maximizing horizontally and vertically
        # we can start with two pointers at our maximum widths,
        # then iterate sideways

        # we can use a global variable to keep track of current max
        
        # we only move one pointer at a time
        # whichever is the smallest current height
        # because any future container will have a smaller width
        # and the height will still be at most heights[i]
        # we can safely discard the smaller one since we cannot produce
        # a larger area than the current pair

        # initialize our two pointers
        left, right = 0, len(heights) - 1
        
        # global variable to hold our current answer
        ans = (right - left) * min(heights[left], heights[right])

        while left < right:
            # calculate current area and update if new max is found
            ans = max(ans, (right - left) * min(heights[left], heights[right]))
            
            # now our pointer updating logic is only shift over whichever is the
            # current smaller height
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        
        return ans