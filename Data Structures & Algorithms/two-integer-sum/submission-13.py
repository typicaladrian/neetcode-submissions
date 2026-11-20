class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # create a dictionary of target-val at given index
        newTarget = {}
        
        for i in range(len(nums)):
            newTarget[target - nums[i]] =  i
        
        print(newTarget)

        for i in range(len(nums)):
            if newTarget.get(nums[i], float('inf')) != float('inf'):
                if i != newTarget[nums[i]]:
                    return [i, newTarget[nums[i]]] 