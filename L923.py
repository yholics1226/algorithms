# [3Sum With Multiplicity] https://leetcode.com/problems/3sum-with-multiplicity/

from collections import Counter
def threeSumMulti(arr, target):
    arr.sort()
    n = len(arr)
    cnt = Counter(arr)
    ans = i = 0
    while i < n:
        ci, j, k = cnt[arr[i]], i, n-1
        while j < k:
            cj, ck = cnt[arr[j]], cnt[arr[k]]
            s = arr[i] + arr[j] + arr[k]
            if s < target:
                j += cj
            elif s > target:
                k -= ck
            else:
                if arr[i] == arr[k]:
                    ans += ci * (ci-1) * (ci-2) // 6
                elif arr[i] == arr[j] < arr[k]:
                    ans += ci * (ci-1) * ck // 2
                elif arr[i] < arr[j] == arr[k]:
                    ans += ci * cj * (cj-1) // 2
                else:
                    ans += ci * cj * ck
                j += cj
                k -= ck
        i += ci
    return ans % 1000000007
