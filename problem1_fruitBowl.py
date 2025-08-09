'''
    Problem Description
    Samaira is playing a mobile game where she needs to connect dots to form a "bowl" that catches falling "fruits".

        The Challenge:

            Bowl Creation: Connect specific dots to create a bowl shape.
            Fruit Catching: The bowl must be designed so that designated "fruit" dots fall directly into it without hitting the edges and being deflected.

        Your Task: Calculate the perimeter of the bowl formed by connecting the dots.

        Accuracy: Round the calculated perimeter to the nearest integer. For example, if the perimeter is 3.5, round it to 4.

    Note: The distance between two coordinates is calculated by using formula:

    sqrt ([(x2 - x1)2 + (y2 - y1)2]) where, (x1, y1) and (x2, y2) are the two coordinates.
'''

import math

def read_points():
    N = int(input())
    points = []
    for _ in range(N):
        x, y = map(int, input().split())
        points.append((x, y))
    return points

def distance(p1, p2):
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

def lower_convex_hull(points):
    points = sorted(points)
    hull = []
    for p in points:
        while len(hull) >= 2 and cross(hull[-2], hull[-1], p) <= 0:
            hull.pop()
        hull.append(p)
    return hull

def cross(o, a, b):
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

def calculate_perimeter(hull):
    perimeter = 0
    for i in range(1, len(hull)):
        perimeter += distance(hull[i-1], hull[i])
    return round(perimeter)

points = read_points()
lower_hull = lower_convex_hull(points)
perimeter = calculate_perimeter(lower_hull)
print(perimeter)

