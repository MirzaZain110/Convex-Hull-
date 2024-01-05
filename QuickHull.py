import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random
#This is QuickElemination Algo result
# Function to determine the side of a point with respect to a line formed by two other points
def find_side(p1, p2, p):
    return (p[1] - p1[1]) * (p2[0] - p1[0]) - (p2[1] - p1[1]) * (p[0] - p1[0])

# Function to find the distance between a point and a line formed by two other points
def find_distance(p1, p2, p):
    return abs((p[1] - p1[1]) * (p2[0] - p1[0]) - (p2[1] - p1[1]) * (p[0] - p1[0]))

# Function to find the points on the convex hull using the Quickhull algorithm
def quickhull(points):
    if len(points) <= 3:
        return points

    min_x = min(points, key=lambda x: x[0])
    max_x = max(points, key=lambda x: x[0])

    hull = []
    hull.append(min_x)
    hull.append(max_x)

    points.remove(min_x)
    points.remove(max_x)

    left_set = []
    right_set = []
    for p in points:
        if find_side(min_x, max_x, p) > 0:
            left_set.append(p)
        elif find_side(min_x, max_x, p) < 0:
            right_set.append(p)

    quickhull_recursive(hull, left_set, min_x, max_x)
    quickhull_recursive(hull, right_set, max_x, min_x)

    return hull

# Recursive function to find the points on the convex hull
def quickhull_recursive(hull, point_set, p1, p2):
    if not point_set:
        return

    max_distance = -1
    farthest_point = None

    for p in point_set:
        distance = find_distance(p1, p2, p)
        if distance > max_distance:
            max_distance = distance
            farthest_point = p

    hull.insert(hull.index(p2), farthest_point)
    point_set.remove(farthest_point)

    left_set = []
    for p in point_set:
        if find_side(p1, farthest_point, p) > 0:
            left_set.append(p)

    right_set = []
    for p in point_set:
        if find_side(farthest_point, p2, p) > 0:
            right_set.append(p)

    quickhull_recursive(hull, left_set, p1, farthest_point)
    quickhull_recursive(hull, right_set, farthest_point, p2)

# Generate random points
def generate_points(num_points):
    points = []
    for _ in range(num_points):
        points.append((random.randint(0, 100), random.randint(0, 100)))
    return points

# Animate convex hull with limited frame size
def animate_convex_hull(num_points):
    points = generate_points(num_points)
    hull = quickhull(points)

    fig, ax = plt.subplots()
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)

    def update(frame):
        nonlocal hull
        if frame < len(hull):
            ax.clear()
            ax.set_xlim(0, 100)  # Set X-axis limit
            ax.set_ylim(0, 100)  # Set Y-axis limit

            # Display all points in blue
            for p in points:
                ax.scatter(p[0], p[1], color='blue')

            # Display only the points forming the convex hull in red
            for i in range(frame + 1):
                ax.plot([hull[i][0], hull[(i + 1) % len(hull)][0]],
                        [hull[i][1], hull[(i + 1) % len(hull)][1]], color='red')
                ax.scatter(hull[i][0], hull[i][1], color='red')

        # Plot the final convex hull in red
        ax.plot([hull[-1][0], hull[0][0]], [hull[-1][1], hull[0][1]], color='red')

    ani = animation.FuncAnimation(fig, update, frames=len(hull) + 1, interval=500)
    plt.show()

# User input for the number of points
# num_points = int(input("Enter the number of points: "))

# Animate the convex hull within limited frame size
# animate_convex_hull(num_points)
animate_convex_hull(10)
