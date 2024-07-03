import matplotlib.pyplot as plt

def mid_point_circle(xc, yc, r):
    """Draws a circle using the Midpoint Circle Algorithm."""

    x = 0
    y = r
    d = 1 - r

    # Plot the initial point
    plt.plot(xc + x, yc + y, 'ro')
    plt.plot(xc - x, yc + y, 'ro')
    plt.plot(xc + x, yc - y, 'ro')
    plt.plot(xc - x, yc - y, 'ro')
    plt.plot(xc + y, yc + x, 'ro')
    plt.plot(xc - y, yc + x, 'ro')
    plt.plot(xc + y, yc - x, 'ro')
    plt.plot(xc - y, yc - x, 'ro')

    # Iterate and plot points
    while x <= y:
        x += 1
        if d < 0:
            d = d + 2 * x + 1
        else:
            d = d + 2 * (x - y) + 1
            y -= 1

        # Plot the eight symmetric points
        plt.plot(xc + x, yc + y, 'ro')
        plt.plot(xc - x, yc + y, 'ro')
        plt.plot(xc + x, yc - y, 'ro')
        plt.plot(xc - x, yc - y, 'ro')
        plt.plot(xc + y, yc + x, 'ro')
        plt.plot(xc - y, yc + x, 'ro')
        plt.plot(xc + y, yc - x, 'ro')
        plt.plot(xc - y, yc - x, 'ro')

    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Midpoint Circle Algorithm')
    plt.grid(True)
    plt.show()

# Example usage:
mid_point_circle(10, 5, 7)  # Center: (10, 5), Radius: 7