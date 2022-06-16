# [멀쩡한 사각형] https://programmers.co.kr/learn/courses/30/lessons/62048

import math
def solution(w,h):
    if w % h == 0:
        return w * h - w
    if h % w == 0:
        return w * h - h
    return w * h - (w + h - math.gcd(w, h))
