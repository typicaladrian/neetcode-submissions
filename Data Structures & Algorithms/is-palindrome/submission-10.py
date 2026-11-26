class Solution:
    def isPalindrome(self, s: str) -> bool:
        '''
            In this problem, we are given a string s and told to return
            whether or not it is a palindrome.

            A brute force solution would be to create a copy of it,
            reverse it, then check for equality. While a time complexity
            of O(n) is optimal in this scenario, the space complexity
            of O(n) is what is suboptimal.

            Our goal is to solve this problem without using any extra space.
            
            This can be easily done by reading from the string forwards and
            backwards at the same time, checking for character equality at each
            point. We do this by using two pointers, resulting in a time
            complexity of O(n) and a space complexity of O(1), no extra space
            used.
        '''

        left, right = 0, len(s) - 1

        while left <= right:
            # skip over non-alphanumeric characters
            if not s[left].isalnum():
                left += 1
                continue
            
            if not s[right].isalnum():
                right -= 1
                continue

            if s[left].lower() != s[right].lower():
                return False
            
            left += 1
            right -= 1
        
        return True