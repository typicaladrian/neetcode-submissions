class Solution:
    def isPalindrome(self, s: str) -> bool:
        # use isalnum() to confirm alphanumeric
        # use lower() to make case insensitive comparisons between characters

        # two pointer problem
        # we can use front/back template since we are dealing with palindromes

        # first remove all non-alphanumeric characters using list comprehension
        # also make everything lowercase since we do not care about case
        #clean_string = [char.lower() for char in s if char.isalnum()]

        front = 0
        back = len(s) - 1

        while front < back:
            while front < back and not s[front].isalnum():
                front += 1
            while back > front and not s[back].isalnum():
                back -= 1
                    
            if s[front].lower() != s[back].lower():
                return False
            
            front += 1
            back -= 1
        
        return True
         