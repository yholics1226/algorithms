# [Summary Ranges] https://leetcode.com/problems/summary-ranges/

def summaryRanges(nums):
    ans = []
    if nums:
        a, b = nums[0], nums[0]-1
        for num in nums:
            if num == b+1:
                b += 1
            else:
                if a == b:
                    ans.append(str(a))
                else:
                    ans.append("{}->{}".format(a, b))
                a = b = num
        if a == b:
            ans.append(str(a))
        else:
            ans.append("{}->{}".format(a, b))
    return ans
