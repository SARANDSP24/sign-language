import matplotlib.pyplot as plt

def dda_line(x1, y1, x2, y2):
    """Draws a line using the DDA algorithm."""

    x, y = x1, y1  # Initialize starting point
    dx = x2 - x1
    dy = y2 - y1

    # Calculate the slope
    m = dy / dx

    # Determine the direction of increment for x and y
    if abs(m) <= 1:
        steps = abs(dx)  # Steps determined by x-direction
        x_inc = 1  # Increment x by 1
        y_inc = m  # Increment y based on slope
    else:
        steps = abs(dy)  # Steps determined by y-direction
        x_inc = 1 / m  # Increment x based on slope
        y_inc = 1  # Increment y by 1

    # Plot the initial point
    plt.plot(x, y, 'ro')  # 'ro' for red circle marker

    # Iterate and plot points
    for i in range(int(steps)):
        x += x_inc
        y += y_inc
        plt.plot(round(x), round(y), 'ro')  # Round to get pixel coordinates

    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('DDA Line Algorithm')
    plt.grid(True)
    plt.show()

# Example usage:
dda_line(2, 3, 10, 7) 