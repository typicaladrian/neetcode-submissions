class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''
            We are given two string, string s and string t,
            and our goal is to return if they are anagrams of
            each other.

            A naive, brute force solution is to just sort both
            strings, but this resutls in an O(nlogn) solution.

            We can do better than this by counting occurrences
            of characters in both strings.

            If we treat the first string as counting up in occurrences
            and the second string as counting down in occurrences,
            then we know that at the end, if they are indeed anagrams,
            the net sum of the character occurrences dataset should be 0
            for all values.

            For this we will use a dictionary. We iterate once through
            each string, and iterate once through the occurrences hashmap.

            This will result in a time complexity of O(n), and a space
            complexity of O(n).
        '''

        from collections import defaultdict

        occurrences = defaultdict(int) # use default dict so we start every new key instance at 0

        for char in s:
            occurrences[char] += 1

        for char in t:
            occurrences[char] -= 1
        
        return all(value == 0 for value in occurrences.values())