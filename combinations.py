from viable import *


def cost(ca, si, be, an):
    c = 0
    c += beams[be][1]
    c += signs[si][1]
    beamL = beams[be][2]
    cableL = beamL / math.cos(an)
    c += cableL * cables[ca][1]
    return c


def case(total_cost, size):
    return total_cost / size


def generate(cablesL, signsL, beamsL, depth):
    best_case = []
    best_case_cost = 8192
    best_case_size = 1
    angle = 0
    for i in range(depth):
        for beam in beamsL:
            for sign in signsL:
                for cable in cablesL:
                    c1 = viable2(cables[cable][0], signs[sign][2], beams[beam][0], beams[beam][2], signs[sign][0], angle)
                    c2 = viable2(cables[cable][0], signs[sign][3], beams[beam][0], beams[beam][2], signs[sign][0], angle)
                    if c1:
                        if case(cost(cable, sign, beam, angle), (signs[sign][2] * signs[sign][3])) < case(best_case_cost, best_case_size):
                            best_case_cost = cost(cable, sign, beam, angle)
                            best_case_size = signs[sign][2] * signs[sign][3]
                            best_case = [cable, sign, beam, angle, case(best_case_cost, best_case_size), (beams[beam][2] / math.cos(angle)), math.cos(angle) * cables[cable][0], (((signs[sign][2] / 2) * signs[sign][0]) + (beams[beam][1] / 2) + 20)]
                    angle += (math.pi / 2) / depth
    return best_case


print(generate(["a", "b", "c", "d", "e", "f"], ["g", "h", "i", "j", "k"], ["l", "m", "n", "o"], 10000))


# Can we use the beam as advertisement area
# If we can, can we use all sides of the sign or just the two faces

# If we have the beam infinitely close to the wall can we
# avoid using brackets and have a infinitely small string so the string wouldn't cost anything

# Can we not use the beam and just attach the sign to the wall

# Is the scaffolding/cable a unit cost or can it be precise

# Does the sign have a width
