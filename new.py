from viable import viable2
from data import *
import math


def generate(cablesL, signsL, beamsL, depth):
    best_case_cost = 100000
    best_case_size = 1
    angle = 0
    distance = 5
    cost = 1000000
    best_case = [best_case_cost, best_case_size, angle, distance]
    for i in range(depth):
        for beam in beamsL:
            for sign in signsL:
                for cable in cablesL:
                    for j in range(depth):
                        c1 = viable2(cables[cable][0], signs[sign][2], beams[beam][0], beams[beam][2], signs[sign][0], angle)
                        if c1:
                            cost = signs[sign][1] + beams[beam][1] + cables[cable][0] * math.sin(angle) * beams[beam][2]
                        if cost < best_case_cost:
                            best_case_size = signs[sign][2] * signs[sign][3]
                            best_case_cost = cost
                        distance -= 5/depth
                        best_case.append([best_case_cost, best_case_size, angle, distance])
                    angle += (math.pi / 2) / depth

    return best_case


print(generate(["a", "b", "c", "d", "e", "f"], ["k"], ["o"], 100))
