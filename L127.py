# [Word Ladder] https://leetcode.com/problems/word-ladder/

from collections import deque
def ladderLength(beginWord, endWord, wordList):
    if endWord not in wordList:
        return 0
    Q = deque([[beginWord, 1]])
    seen = {beginWord}
    while Q:
        [word, num] = Q.popleft()
        if word == endWord:
            return num
        for nw in wordList:
            if nw not in seen:
                n = 0
                for i in range(len(beginWord)):
                    if word[i] != nw[i]:
                        n += 1
                        if n > 1:
                            break
                else:
                    if n == 1:
                        Q.append([nw, num + 1])
                        seen.add(nw)
    return 0

# refactor 1
def ladderLength1(beginWord, endWord, wordList):
    if endWord not in wordList:
        return 0
    wlset = set(wordList)
    bset = {beginWord}
    eset = {endWord}
    lv = 1
    while wlset:
        wlset -= bset
        tmp = set()
        for w in bset:
            if w in eset:
                return lv
            for nw in wlset:
                n = 0
                for i in range(len(w)):
                    if w[i] != nw[i]:
                        n += 1
                        if n > 1:
                            break
                else:
                    tmp.add(nw)
        if not tmp:
            return 0
        bset = tmp
        lv += 1
        if len(bset) > len(eset):
            bset, eset = eset, bset

# refactor 2
def ladderLength2(beginWord, endWord, wordList):
    if endWord not in wordList:
        return 0
    wlset = set(wordList)
    bset = {beginWord}
    eset = {endWord}
    lv = 2
    while wlset:
        wlset -= bset
        tmp = set()
        for w in bset:
            for i in range(len(w)):
                for x in 'abcdefghijklmnopqrstuvwxyz':
                    nw = w[:i] + x + w[i+1:]
                    if nw in eset:
                        return lv
                    if nw in wlset:
                        tmp.add(nw)
        if not tmp:
            return 0
        bset = tmp
        lv += 1
        if len(bset) > len(eset):
            bset, eset = eset, bset
