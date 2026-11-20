class Solution:
    def isPalindrome(self, s: str) -> bool:
        # use isalnum() to confirm alphanumeric
        # use lower() to make case insensitive comparisons between characters

        # two pointer problem
        # we can use front/back template since we are dealing with palindromes

        # first remove all non-alphanumeric characters using list comprehension
        # also make everything lowercase since we do not care about case
        clean_string = [char.lower() for char in s if char.isalnum()]

        front = 0
        back = len(clean_string) - 1

        for i in range(len(clean_string)):
            if clean_string[front] != clean_string[back]:
                return False
            
            if front != back and front < back:
                front += 1
                back -= 1
        
        return True
         