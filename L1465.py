# [Maximum Area of a Piece of Cake After Horizontal and Vertical Cuts] https://leetcode.com/problems/maximum-area-of-a-piece-of-cake-after-horizontal-and-vertical-cuts/

def maxArea(h, w, horizontalCuts, verticalCuts):
    horizontalCuts.sort()
    verticalCuts.sort()
    hd, vd = horizontalCuts[0], verticalCuts[0]
    horizontalCuts.append(h)
    verticalCuts.append(w)
    for i in range(1, len(horizontalCuts)):
        hd = max(hd, horizontalCuts[i] - horizontalCuts[i-1])
    for i in range(1, len(verticalCuts)):
        vd = max(vd, verticalCuts[i] - verticalCuts[i-1])
    return (hd * vd) % 1000000007
