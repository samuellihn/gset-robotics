import math


def vec2_to_tank(input_vec: (float, float), scale=900) -> (float, float):
    x = -input_vec[0] # x is representing turning
    y = input_vec[1] # y is representing speed

    v = (1 - abs(x)) * y + y
    w = (1 - abs(y)) * x + x
    right = (v + w) / 2
    left = (v - w) / 2
    right *= scale
    left *=scale


    return right, left

def clamp(val, minimum, maximum):
    return max(minimum, min(maximum, val))