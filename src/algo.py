import random
import math

def randomCoordinate(n):
    coordinate = []
    for i in range(n):
        coordinate.append(round(random.uniform(-1000, 1000), 2))
    
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


def selectionSort(points):  # Sort by x-axis value
    for i in range(len(points)):
        temp = []
        min = points[i][0]
        min_idx = i
        for j in range(i, len(points)):
            if(points[j][0] < min):
                min = points[j][0]
                min_idx = j

        # Swap
        temp = points[i]
        points[i] = points[min_idx]
        points[min_idx] = temp


def divideAndConquer(points):
    n = len(points)
    if (n == 2):    # Base case 1
        return (points[0], points[1], distance(points[0], points[1]))
    
    if (n == 3):    # Base case 2
        min_dist = distance(points[0], points[1])  
        dist2 = distance(points[0], points[2])
        dist3 = distance(points[1], points[2])
        closest_point1 = points[0]
        closest_point2 = points[1]

        if(dist2 < min_dist):
            min_dist = dist2
            closest_point1 = points[0]
            closest_point2 = points[2]
        if(dist3 < min_dist):
             min_dist = dist3
             closest_point1 = points[1]
             closest_point2 = points[2]
             
        return (closest_point1, closest_point2, min_dist)

    # Recursion
    mid = n // 2
    leftPoints = points[:mid]
    rightPoints = points[mid:]

    point1_1, point2_1, dist1 = divideAndConquer(leftPoints)
    point1_2, point2_2, dist2 = divideAndConquer(rightPoints)

    closest_point1 = []
    closest_point2 = []
    min_dist = 0

    if(dist1 < dist2):
        min_dist = dist1
        closest_point1 = point1_1
        closest_point2 = point2_1
    else:
        min_dist = dist2
        closest_point1 = point1_2
        closest_point2 = point2_2

    if (n % 2 == 0):
        mid = (points[mid-1][0] + points[mid][0]) / 2
    else:
        mid = points[mid][0]

    tempPoints = []
    for i in range(len(leftPoints)):
        if (leftPoints[i][0] >= mid - min_dist):
            tempPoints.append(leftPoints[i])

    for i in range(len(rightPoints)):
        if (rightPoints[i][0] <= mid + min_dist):
            tempPoints.append(rightPoints[i])

    for i in range(len(tempPoints)):
        for j in range(i+1, len(tempPoints)):
            tempDist = distance(tempPoints[i], tempPoints[j])
            if (tempDist < min_dist):
                min_dist = tempDist
                closest_point1 = tempPoints[i]
                closest_point2 = tempPoints[j]

    return (closest_point1, closest_point2, min_dist)