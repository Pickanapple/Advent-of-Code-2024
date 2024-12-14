from functools import cache, lru_cache

@cache
def distance(index1: tuple, index2: tuple):
    return ((index1[0] - index2[0])**2 + (index1[1] - index2[1])**2) ** (1/2)

@cache
def findFunction(point1: tuple, point2: tuple):
    gradiant = (point2[0] - point1[0]) / (point2[1] - point1[1]) #Our 2d list has y before x

    #y - y1 = m(x - x1)
    return lambda x: gradiant * x - (gradiant * point1[1] + point1[0])

def findAntiNode(listToUse):
    pass