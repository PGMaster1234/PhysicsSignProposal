from data import *
import math


def viable(sign, beam, cable, c):
    ang = []
    output = []
    output_ang = []
    for i in range(c):
        # print(i * math.pi / (c * 2 + 0.001))
        ang.append(i * math.pi / (c * 2 + 0.001))

    for a in ang:
        # print(a)
        # print(sign + beam + 20)
        # print(math.sin(a) * cable)
        if (math.sin(a) * cable) > (sign + beam + 20):
            # print("not popped")
            output.append(math.sin(a) * cable)
            output_ang.append(a)
        else:
            pass
            # print("pop")
            # print("cable strength: " + str(math.sin(a) * cable))

    # for i, angle in enumerate(ang):
    #     ang[i] = angle / math.pi
    #     ang[i] = angle * 180

    return ang, output, output_ang


# print(viable(signs["i"][0], beams["n"][0], cables["c"][0], 50)[1])

def viable2(cable_strength, sign_width, beam_weight, beam_length, sign_weight, angle):
    if (math.sin(angle) * cable_strength * beam_length) > (((sign_width * sign_weight) / 2) + (beam_length * beam_weight / 2) + 20):
        return True
    else:
        return False


# print(viable2(100, 1, 50, 2, 100, math.pi / 4))
