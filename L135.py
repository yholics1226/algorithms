# [Candy] https://leetcode.com/problems/candy/

def candy(ratings):
    n = len(ratings)
    sr = sorted([(r, i) for i, r in enumerate(ratings)])
    candies = [1] * n + [0]
    for _, i in sr:
        if i > 0 and ratings[i] > ratings[i-1]:
            candies[i] = max(candies[i-1], candies[i+1]) + 1
        elif i < n-1 and ratings[i] > ratings[i+1]:
            candies[i] = candies[i+1] + 1
    return sum(candies)

# w/o sorting
def candy(ratings):
    ans = cur = 1
    last_peak_idx, last_peak_candy = 0, 1
    for i in range(1, len(ratings)):
        if ratings[i] > ratings[i-1]:
            cur += 1
            ans += cur
            last_peak_idx = i
            last_peak_candy = cur
        elif ratings[i] < ratings[i-1]:
            cnt = i - last_peak_idx
            if cnt == last_peak_candy:
                last_peak_candy += 1
                ans += 1
            ans += cnt
            cur = 1
        else:
            ans += 1
            last_peak_idx = i
            last_peak_candy = cur = 1
    return ans
