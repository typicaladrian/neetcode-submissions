class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevDict = {} # val : idx
        for i in range(len(nums)):
            rem = target - nums[i]
            # if the remainder is in the dict already, then we can return tuple
            if rem in prevDict:
                return [prevDict[rem], i]
            # if remainder is not in dict, add curr num:idx to dict
            prevDict[nums[i]] = i

        # space complexity too high for solution below! :(
        # # create a dictionary of target-val at given index
        # remainders = {}
        
        # for i in range(len(nums)):
        #     remainders[target - nums[i]] =  i

        # for i in range(len(nums)):
        #     if remainders.get(nums[i], float('inf')) != float('inf'):
        #         if i != remainders[nums[i]]:
        #             return [i, remainders[nums[i]]] 