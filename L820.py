# [Short Encoding of Words] https://leetcode.com/problems/short-encoding-of-words/

def minimumLengthEncoding(words):
    words.sort(key=len, reverse=True)
    ans = 0
    seen = set()
    for word in words:
        if (word + '#') in seen:
            continue
        n = len(word)
        ans += n+1
        for i in range(n):
            seen.add(word[i:] + '#')
    return ans

# another solution
def minimumLengthEncoding(words):
    words = sorted(word[::-1] for word in set(words)) + ['']
    ans = 0
    curr = ''
    for word in words:
        if not word.startswith(curr):
            ans += len(curr) + 1
        curr = word  
    return ans
