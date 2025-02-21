import math


def simple_sine(angle):
    if angle == 0:
        return 0
    elif angle == 30:
        return round(1 / 2, 2)
    elif angle == 45:
        return round(math.sqrt(2) / 2, 2)
    elif angle == 60:
        return round(math.sqrt(3) / 2, 2)
    elif angle == 90:
        return 1
    elif angle == 180:
        return 0
    elif angle == 270:
        return -1
    elif angle == 360:
        return 0
    else:
        return -99


def simple_cosine(angle):
    if angle == 0:
        return 1
    elif angle == 30:
        return round(math.sqrt(3) / 2, 2)
    elif angle == 45:
        return round(math.sqrt(2) / 2, 2)
    elif angle == 60:
        return round(1 / 2, 2)
    elif angle == 90:
        return 0
    elif angle == 180:
        return -1
    elif angle == 270:
        return 0
    elif angle == 360:
        return 1
    else:
        return -99