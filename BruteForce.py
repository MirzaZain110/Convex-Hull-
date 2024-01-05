import numpy as np
import numpy as np
import matplotlib.pyplot as plt
import time
#This algo is BruteForce Result
# Use cross product to determine whether a point lies above or below a line.
def is_above(p, a, b):
    return np.cross(p - a, b - a) < 0

points = []

def initPoints(n):
    for i in range(n):
        points.append([np.random.randint(1, 100), np.random.randint(1, 100)])
        plt.plot(points[i][0], points[i][1], marker="o", color="k")

def convexHull(arr):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            above = 0
            below = 0
            for k in range(len(arr)):
                if k != i and k != j:
                    if is_above(np.array(arr[k]), np.array(arr[i]), np.array(arr[j])):
                        above += 1
                    else:
                        below += 1
                if k == len(arr) - 1 and (below == 0 or above == 0):
                    x_values = [arr[i][0], arr[j][0]]
                    y_values = [arr[i][1], arr[j][1]]
                    plt.plot(x_values, y_values)
                    plt.pause(0.5)  # Adjust the pause time (in seconds) as needed

plt.figure()
num = int(input("Enter the number of points: "))
initPoints(num) # enter points
convexHull(points)

plt.show()
