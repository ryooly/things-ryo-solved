def twistEngine(word1, word2):
    result = ""
    for i in range(len(word1 + word2)):
        


class Solution(object):
    def mergeAlternately(self, word1, word2):
        if 1 <= len(word1) <= 100 and 1 <= len(word2) <= 100:
            result = twistEngine(word1, word2)
            return result
        else:
            return "input not valid"


parents = Solution()
result = parents.mergeAlternately("england", "football")
print(result)


# pake looping ganjil genap apabila emang sala satunya udah abis tinggal push push aja 

# im stuck btw 