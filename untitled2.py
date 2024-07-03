import matplotlib.pyplot as plt

def bresenham_line(x1, y1, x2, y2):
    """Draws a line using Bresenham's algorithm."""

    dx = abs(x2 - x1)
    dy = abs(y2 - y1)

    # Determine the initial decision parameter
    p = 2 * dy - dx

    # Initialize the starting pixel
    x = x1
    y = y1

    # Plot the initial point
    plt.plot(x, y, 'ro')

    # Iterate and plot points
    for i in range(dx):
        plt.plot(x, y, 'ro')
        if p < 0:
            p += 2 * dy
        else:
            p += 2 * (dy - dx)
            y += 1 if y1 < y2 else -1  # Increment y based on slope
        x += 1

    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Bresenham Line Algorithm')
    plt.grid(True)
    plt.show()

# Example usage:
bresenham_line(5,5, 10, 10)