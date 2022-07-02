# [Maximum Units on a Truck] https://leetcode.com/problems/maximum-units-on-a-truck/

def maximumUnits(boxTypes, truckSize):
    boxTypes.sort(key=lambda x: x[1], reverse=True)
    ans = 0
    for b, u in boxTypes:
        if b <= truckSize:
            ans += b * u
            truckSize -= b
        else:
            ans += truckSize * u
            break
    return ans
