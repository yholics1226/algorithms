# [Count Sorted Vowel Strings] https://leetcode.com/problems/count-sorted-vowel-strings/

def countVowelStrings(n):
    # Mathematically, the answer is H(5,n) = C(n+4,n) = C(n+4,4)
    return (n+4) * (n+3) * (n+2) * (n+1) // 24  # math.comb(n+4, 4)

# another solution
def countVowelStrings(n):
    res = [1] * 5
    for _ in range(n-1):
        for i in range(1, 5):
            res[i] += res[i-1]
    return sum(res)
