import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import random
#This Swwpline Algo
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def orientation(p, q, r):
    val = (q.y - p.y) * (r.x - q.x) - (q.x - p.x) * (r.y - q.y)
    if val == 0:
        return 0
    return 1 if val > 0 else 2

def convex_hull(points):
    n = len(points)
    if n < 3:
        return points

    hull = []
    l = 0
    for i in range(1, n):
        if points[i].x < points[l].x:
            l = i

    p = l
    while True:
        hull.append(points[p])
        q = (p + 1) % n

        for i in range(n):
            if orientation(points[p], points[i], points[q]) == 2:
                q = i

        p = q

        if p == l:
            break

    return hull

def animate(i):
    plt.clf()
    if i < len(lines):
        plt.plot([lines[i][0].x, lines[i][1].x], [lines[i][0].y, lines[i][1].y], color='orange', linestyle='-', linewidth=2)
        for point in points:
            plt.plot(point.x, point.y, 'bo')
    else:
        for point in hull_points:
            plt.plot(point.x, point.y, 'ro')
        for i in range(len(hull_points)):
            plt.plot([hull_points[i].x, hull_points[(i + 1) % len(hull_points)].x],
                     [hull_points[i].y, hull_points[(i + 1) % len(hull_points)].y], color='green', linestyle='-', linewidth=2)

points = [Point(random.uniform(0, 10), random.uniform(0, 10)) for _ in range(10)]  # Generate 10 random points

points.sort(key=lambda p: p.x)

lines = [(points[i], points[i + 1]) for i in range(len(points) - 1)]

hull_points = convex_hull(points)

fig = plt.figure()
ani = animation.FuncAnimation(fig, animate, frames=len(lines) + 10, interval=500, repeat=False)
plt.show()
