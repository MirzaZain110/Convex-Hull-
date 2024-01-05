import tkinter as tk

def orientation(p, q, r):
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:
        return 0  # Collinear
    return 1 if val > 0 else 2  # Clockwise or counterclockwise

def on_segment(p, q, r):
    return (q[0] <= max(p[0], r[0]) and q[0] >= min(p[0], r[0]) and
            q[1] <= max(p[1], r[1]) and q[1] >= min(p[1], r[1]))

def do_intersect(p1, q1, p2, q2):
    o1 = orientation(p1, q1, p2)
    o2 = orientation(p1, q1, q2)
    o3 = orientation(p2, q2, p1)
    o4 = orientation(p2, q2, q1)

    if o1 != o2 and o3 != o4:
        return True  # Intersecting

    if o1 == 0 and on_segment(p1, p2, q1):
        return True

    if o2 == 0 and on_segment(p1, q2, q1):
        return True

    if o3 == 0 and on_segment(p2, p1, q2):
        return True

    if o4 == 0 and on_segment(p2, q1, q2):
        return True

    return False  # Not intersecting

class LineIntersectApp:
    def __init__(self, root):  # Fixed typo: It should be __init__, not init
        self.root = root
        self.root.title("Line Segment Intersection Checker")

        self.canvas = tk.Canvas(root, width=400, height=400, bg="white")
        self.canvas.pack()

        self.points = []

        self.canvas.bind("<Button-1>", self.on_click)

    def on_click(self, event):
        x, y = event.x, event.y
        self.points.append((x, y))
        self.canvas.create_oval(x - 3, y - 3, x + 3, y + 3, fill="black")

        if len(self.points) == 4:
            p1, q1, p2, q2 = self.points

            # Draw line segments
            self.canvas.create_line(p1, q1, fill="blue")
            self.canvas.create_line(p2, q2, fill="green")

            if do_intersect(p1, q1, p2, q2):
                result_text = "The two line segments intersect."
            else:
                result_text = "The two line segments do not intersect."

            self.canvas.create_text(200, 380, text=result_text, font=("Helvetica", 12), fill="red")

if __name__ == "__main__":
    root = tk.Tk()
    app = LineIntersectApp(root)
    root.mainloop()
