def twistEngine(word1, word2):
    w1 = word1
    w2 = word2

    result = ""

    for i in range(max(len(w1), len(w2))):
        if i < len(w1):
            result += w1[i]
        
        if i < len(w2):
            result += w2[i]
    
    return result


class Solution(object):
    def mergeAlternately(self, word1, word2):
        if 1 <= len(word1) <= 100 and 1 <= len(word2) <= 100:
            result = twistEngine(word1, word2)
            return result
        else:
            return "input not valid"


parents = Solution()
result = parents.mergeAlternately("satu", "dua")
print(result)