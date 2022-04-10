# [Top K Frequent Elements] https://leetcode.com/problems/top-k-frequent-elements/

from collections import Counter
def topKFrequent(nums, k):
    nH = Counter(nums)
    return [num for num, _ in sorted(nH.items(), key=lambda x: -x[1])[:k]]

# another solution using heap
import heapq
from collections import Counter
def topKFrequent(nums, k):
    nH = Counter(nums)
    hq = []
    nums = set(nums)
    for num in nums:
        heapq.heappush(hq, (-nH[num], num))
    ans = []
    for _ in range(k):
        ans.append(heapq.heappop(hq)[1])
    return ans
