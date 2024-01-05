import tkinter as tk
import math
from functools import cmp_to_key
import timeit
from tkinter import simpledialog
# one more Quikhull ALgo code 
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def orientation(p, q, r):
    val = (q.y - p.y) * (r.x - q.x) - (q.x - p.x) * (r.y - q.y)
    if val == 0:
        return 0  # collinear
    return 1 if val > 0 else -1  # clockwise or counterclockwise

def compare(p1, p2):
    angle1 = math.atan2(p1.y - pivot.y, p1.x - pivot.x)
    angle2 = math.atan2(p2.y - pivot.y, p2.x - pivot.x)

    if angle1 < angle2:
        return -1
    elif angle1 > angle2:
        return 1
    else:
        return 0

class ConvexHullApp:
    def __init__(self, root):
        self.points = []
        self.canvas = tk.Canvas(root, bg="white")
        self.canvas.pack(expand=tk.YES, fill=tk.BOTH)

        self.label = tk.Label(root, text="Click on the canvas to add points, then press 'Compute Convex Hull'")
        self.label.pack()

        self.compute_button = tk.Button(root, text="Compute Convex Hull", command=self.compute_convex_hull)
        self.compute_button.pack()

        self.canvas.bind("<Button-1>", self.on_click_button)

    def on_click_button(self, event):
        num_points = simpledialog.askinteger("Input", "Enter the number of points:")
        if num_points is not None and num_points >= 3:
            for _ in range(num_points):
                x = simpledialog.askfloat("Input", "Enter x coordinate:")
                y = simpledialog.askfloat("Input", "Enter y coordinate:")
                self.points.append(Point(x, y))
                self.canvas.create_oval(x - 3, y - 3, x + 3, y + 3, fill="blue")

            # Adjust canvas size based on maximum coordinates
            max_x = max(point.x for point in self.points)
            max_y = max(point.y for point in self.points)
            canvas_width = max(500, max_x + 10)
            canvas_height = max(500, max_y + 10)
            self.canvas.config(width=canvas_width, height=canvas_height)

            # Scale factor for better visualization
            scale_factor = min(canvas_width / 20, canvas_height / 20)

            # Redraw points with proper spacing
            self.canvas.delete("all")
            for p in self.points:
                scaled_x = p.x * scale_factor
                scaled_y = p.y * scale_factor
                self.canvas.create_oval(scaled_x - 3, scaled_y - 3, scaled_x + 3, scaled_y + 3, fill="blue")

    def compute_convex_hull(self):
        if len(self.points) < 3:
            self.label.config(text="At least 3 points are required to compute convex hull.")
            return

        # Record start time using timeit
        start_time = timeit.default_timer()

        convex_hull = self.quick_elimination(self.points)

        # Record end time using timeit
        end_time = timeit.default_timer()

        # Calculate execution time in seconds
        execution_time = (end_time - start_time)

        # Clear canvas and draw convex hull
        self.canvas.delete("all")

        # Scale factor for better visualization
        scale_factor = min(self.canvas.winfo_width() / 20, self.canvas.winfo_height() / 20)

        for p in self.points:
            scaled_x = p.x * scale_factor
            scaled_y = p.y * scale_factor
            self.canvas.create_oval(scaled_x - 3, scaled_y - 3, scaled_x + 3, scaled_y + 3, fill="blue")

        for i in range(len(convex_hull) - 1):
            x1 = convex_hull[i].x * scale_factor
            y1 = convex_hull[i].y * scale_factor
            x2 = convex_hull[i + 1].x * scale_factor
            y2 = convex_hull[i + 1].y * scale_factor
            self.canvas.create_line(x1, y1, x2, y2, fill="red")

        x1 = convex_hull[-1].x * scale_factor
        y1 = convex_hull[-1].y * scale_factor
        x2 = convex_hull[0].x * scale_factor
        y2 = convex_hull[0].y * scale_factor
        self.canvas.create_line(x1, y1, x2, y2, fill="red")

        self.label.config(text=f"Convex Hull Computed! Execution Time: {execution_time:.6f} seconds")

    def quick_elimination(self, points):
        global pivot
        pivot = min(points, key=lambda point: (point.y, point.x))
        sorted_points = sorted(points, key=cmp_to_key(compare))

        convex_hull = []
        for point in sorted_points:
            while len(convex_hull) >= 2 and orientation(convex_hull[-2], convex_hull[-1], point) != -1:
                convex_hull.pop()
            convex_hull.append(point)

        return convex_hull

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Convex Hull - Quick Elimination")
    app = ConvexHullApp(root)
    root.geometry("600x600")
    root.mainloop()

