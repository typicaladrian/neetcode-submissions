class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # not the same length = not an anagram
        if len(s) != len(t):
            return False

        countS, countT = {}, {}
        for i in range(0, len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        
        for char in countS.keys():
            if countS[char] != countT.get(char, 0):
                return False

        return True




