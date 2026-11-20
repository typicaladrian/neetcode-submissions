class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            longestString = s
            shorterString = t
        else:
            longestString = t
            shorterString = s
        for char in longestString:
            # if character does not appear in t, not an anagram
            if shorterString.count(char) == 0:
                return False
            else:
                if longestString.count(char) != shorterString.count(char):
                    return False
        return True
            
        
        # counts = {}
        # for char in s:
        #     if char in counts.keys():
        #         counts[char] += 1
        #     else:
        #         counts[char] = 1
        # print(counts)
        
        # for char in t:
        #     if char in counts.keys():

            