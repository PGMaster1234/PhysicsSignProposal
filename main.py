from data import *
import math


def calculate(cab_len, ang):
    cost = cab_len * math.sin(ang) + (5 * math.ceil(cab_len * math.sin(ang)))
    return cost


def optimize(starting):
    pass
