class Solution:
    def maxArea(self, heights: List[int]) -> int:
        '''
            In this problem, we are given an integer array of heights
            where height[i] represents the height of the ith bar.

            Our goal is to return the maximum amount of water a container

            For this problem, a simple naive solution would be to calculate every
            possible combination of containers that we can make.
            However, this results in a time complexity of O(n^2). We can do better.

            First thing to note is how are we going to calculate our area
            at a given two heights.

            We can calculate area at a given height by using the formula:
                min(leftHeight, rightHeight) * (rightIndex - leftIndex)

            Now, of course, we see we will need two pointers, and they will
            work inwards, calculating area at a given height at each point.

            We always decide to bring the smallest height inwards because
            a given area, any future container will have a smaller width, with
            its height still at most that given smallest height. This means
            that we cannot produce an area larger than the current pair, so
            we can safely discard the smaller height and move that pointer inwards.
        '''

        # instantiate left and right pointers
        left, right = 0, len(heights) - 1

        maxArea = 0
        while left < right:
            currArea = min(heights[left], heights[right]) * (right - left)
            maxArea = max(maxArea, currArea)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
       
        return maxArea