class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        '''
            In koko eating bananas, we are given an integer array of piles,
            where piles[i] is the number of bananas in the ith pile.

            In essence, we are tasked to find the minimum speed k that we must eat bananas
            within the hours h.

            A key point is that we cannot start eating bananas from another pile, even if you finish
            all the bananas in a pile early.

            A naive approach would be to go through every possible speed, going up from a speed of
            1 banana per hour, and find the breaking point at which we can finish all bananas.
            However, this time complexity will be O(n)

            We can do better by halving our search for a minimum k each time.
            What does this sound like to you? Binary search of course
        '''
        # Step 2: Define our conditional function, timeSpent(mid)
        def timeSpent(speed) -> bool:
            hoursSpent = 0
            for pile in piles:
                hoursSpent += math.ceil(pile / speed)
            
            return hoursSpent <= h


        # Step 1: Define our binary search
        # Our bounds will be 1 to max(piles), since the slowest koko can eat is 1 banana per second
        # and the fastest koko can eat without eating unneccesarily fast is max(piles) since we will
        # at best finish one pile an hour.

        left, right = 1, max(piles)

        while left < right:
            mid = left + (right - left) // 2 # using (right - left) here to account for integer overflow, even though we have no need to worry about this in python

            # NOTE: we write our condition function, timeSpent(mid), here and we will define that function in step 2
            if timeSpent(mid):
                right = mid
            else:
                left = mid + 1

        return left     
