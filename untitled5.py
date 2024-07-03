import matplotlib.pyplot as plt

def draw_triangle(vertices):
    """Draws a triangle."""
    x = [vertex[0] for vertex in vertices]
    y = [vertex[1] for vertex in vertices]
    plt.plot(x, y, 'ro-')  # 'ro-' for red circles connected by lines

def draw_rectangle(bottom_left, width, height):
    """Draws a rectangle."""
    x = [bottom_left[0], bottom_left[0] + width, bottom_left[0] + width, bottom_left[0], bottom_left[0]]
    y = [bottom_left[1], bottom_left[1], bottom_left[1] + height, bottom_left[1] + height, bottom_left[1]]
    plt.plot(x, y, 'bo-')  # 'bo-' for blue circles connected by lines

def draw_square(bottom_left, side_length):
    """Draws a square."""
    draw_rectangle(bottom_left, side_length, side_length)

def draw_parallelogram(bottom_left, width, height, angle_degrees):
    """Draws a parallelogram."""
    angle_radians = angle_degrees * (3.14159 / 180)  # Convert degrees to radians
    x = [bottom_left[0], bottom_left[0] + width, bottom_left[0] + width + height * math.sin(angle_radians),
         bottom_left[0] + height * math.sin(angle_radians), bottom_left[0]]
    y = [bottom_left[1], bottom_left[1], bottom_left[1] + height * math.cos(angle_radians),
         bottom_left[1] + height * math.cos(angle_radians), bottom_left[1]]
    plt.plot(x, y, 'go-')  # 'go-' for green circles connected by lines

# Example usage:
plt.figure(figsize=(6, 6))
plt.xlabel('X')
plt.ylabel('Y')
plt.title('2D Shapes')
plt.grid(True)

# Draw a triangle
draw_triangle([(2, 1), (5, 4), (1, 4)])

# Draw a rectangle
draw_rectangle((1, 1), 4, 3)

# Draw a square
draw_square((6, 1), 3)

# Draw a parallelogram
import math  # Import math module for trigonometric functions
draw_parallelogram((1, 6), 4, 2, 45)  # 45 degrees angle

plt.axis('equal')  # Ensure shapes appear with the correct aspect ratio
plt.show()