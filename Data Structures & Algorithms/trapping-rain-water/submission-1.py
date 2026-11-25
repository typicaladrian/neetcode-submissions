class Solution:
    def trap(self, height: List[int]) -> int:
        '''
            The given array height represents an elevation map, where each value
            height[i] represents the height of a bar.

            Our goal is to return the total amount of water that can be trapped
            between the bars.

            From the diagram we can see that calculating the amount of water trapped
            at each index i can be easily done.

            The amount of water trapped at each index i can be found using the following
            equation:
                min(maxLeft, maxRight) - height[i]
            where maxLeft is the maximum height to the left of i
            and maxRight is the maximum height to the right of i

            Now, a easy solution that comes to mind is to create two arrays,
            each holding the maxLeft and maxRights at each i, then calculate
            water trapped at each i and sum them all together. This is a great
            solution for time complexity, which is O(n), but in terms of space
            complexity it is not the best. Since we are storing n terms in the arrays
            of maxLefts and maxRights, our space complexity will be O(2n) = O(n).

            Is there a better way to do this where our space complexity is O(1)?

            We can try an approach with two pointers, where we store a running
            leftMax and rightMax.

            We first determine which side is our current bottleneck, either
            the left or the right side being the smallest side.

            Then, we compare our current height at the bottlenecked side to our
            current max on the side of our bottleneck (ex height[left] >= leftMax).

            If our current height is greater (height[left] >= leftMax), then
            we simply update our current max, because we have went up in height
            and water simply cannot pool on top of a new peak. Then move the index
            up.

            If it is less, then there is a dip! We can calculate current water
            pooled at this index, knowing that water is at most at height[left]
            but guaranteed to be trapped at some point by height[right].

            Adding in this situation can be done by the equation
                leftMax - height[left]
           
            Lastly we move the pointer over on the bottlenecked side.
        '''

        left, right = 0, len(height) - 1
        leftMax, rightMax = 0, 0
        water = 0

        while left < right:
            if height[left] < height[right]:
                if height[left] >= leftMax:
                    leftMax = height[left]
                else:
                    water += leftMax - height[left]
                left += 1
            else:
                if height[right] >= rightMax:
                    rightMax = height[right]
                else:
                    water += rightMax - height[right]
                right -= 1

        return water