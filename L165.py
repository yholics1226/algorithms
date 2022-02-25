# [Compare Version Numbers] https://leetcode.com/problems/compare-version-numbers/

def compareVersion(version1, version2):
    v1 = [*map(int, version1.split('.'))]
    v2 = [*map(int, version2.split('.'))]
    n1, n2 = len(v1), len(v2)
    for i in range(max(n1, n2)):
        i1 = v1[i] if i < n1 else 0
        i2 = v2[i] if i < n2 else 0
        if i1 < i2:
            return -1
        elif i1 > i2:
            return 1
    return 0
