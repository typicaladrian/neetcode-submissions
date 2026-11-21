class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft, maxRight = [0]*len(height), [0]*len(height)

        # iterating forwards to obtain all maxLefts
        maxLeft[0] = height[0]
        for i in range(1, len(height)):
            maxLeft[i] = max(maxLeft[i-1], height[i])

        # iterating backwards to obtain all maxRights
        maxRight[len(height)-1] = height[len(height)-1]
        for i in range(len(height)-2, -1, -1):
            maxRight[i] = max(maxRight[i+1], height[i])

        total = 0
        for i in range(0, len(height)):
            total += min(maxLeft[i], maxRight[i]) - height[i]
        
        return total