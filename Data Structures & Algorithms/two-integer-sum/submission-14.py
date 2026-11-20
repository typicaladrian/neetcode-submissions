class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # create a dictionary of target-val at given index
        remainders = {}
        
        for i in range(len(nums)):
            remainders[target - nums[i]] =  i

        for i in range(len(nums)):
            if remainders.get(nums[i], float('inf')) != float('inf'):
                if i != remainders[nums[i]]:
                    return [i, remainders[nums[i]]] 