class Solution:
    def findMin(self, nums: List[int]) -> int:
        # answer: if we take the mid each time, the left most value
                  

        # if nums[left] >= nums[mid], search right
        # else search left

        # if at any point nums[left] < nums right, then we are in
        # sorted portion of array, simply return nums[left]

        left = 0
        right = len(nums) - 1
        result = nums[0]

        while left <= right:
            if nums[left] < nums[right]:
                result = min(result, nums[left])
                break

            mid = (left + right) // 2
            result = min(result, nums[mid])
            if nums[mid] >= nums[left]:
                left = mid + 1
            else:
                right = mid - 1
            
        return result