# [Count All Valid Pickup and Delivery Options] https://leetcode.com/problems/count-all-valid-pickup-and-delivery-options/

import math
def countOrders(n):
    # return (math.factorial(2*n) // (2**n)) % (10**9 + 7)
    return (math.factorial(2*n) >> n) % (10**9 + 7)
