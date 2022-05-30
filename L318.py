# [Maximum Product of Word Lengths] https://leetcode.com/problems/maximum-product-of-word-lengths/

def maxProduct(words):
    def isUnique(s1, s2):
        for x in s1:
            if x in s2:
                return False
        return True
    answer = 0
    for i in range(len(words)-1):
        for j in range(i+1, len(words)):
            if isUnique(words[i], words[j]):
                tmp = len(words[i]) * len(words[j])
                answer = max(answer, tmp)
    return answer
