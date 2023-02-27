import random as rand
import math

def randomCoordinate(n):
    coordinate = []
    for i in range(n):
        coordinate.append(round(rand.uniform(-1000, 1000), 2))
    
    return coordinate

def distance(point1, point2):
    res = 0
    for i in range(len(point1)):
        res += (point1[i] - point2[i]) ** 2
    
    return math.sqrt(res)


def bruteForce(points):
    closest_pair_distance = 999999999
    closest_point1 = points[0]
    closest_point2 = points[1]
    for i in range(len(points)):
        for j in range(len(points)):
            dist = distance(points[i], points[j])
            if (i != j and dist <= closest_pair_distance):
                closest_pair_distance = dist
                closest_point1 = points[i]
                closest_point2 = points[j]

    return (closest_point1, closest_point2, closest_pair_distance)